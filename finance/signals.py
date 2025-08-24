from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Payment, TenantAccount, Invoice

def recalc_tenant_account(tenant):
    # 1) Update each invoice status based on its payments (no .save() here)
    for invoice in tenant.invoices.all():
        total_paid = sum(p.amount for p in invoice.payments.all())
        if total_paid >= invoice.amount_due:
            new_status = "paid"
        elif total_paid > 0:
            new_status = "partial"
        else:
            new_status = "unpaid"

        if invoice.status != new_status:
            # Use .update() so NO signals fire (prevents recursion)
            Invoice.objects.filter(pk=invoice.pk).update(status=new_status)

    # 2) Update tenant account balance
    account, _ = TenantAccount.objects.get_or_create(tenant=tenant)
    total_invoices = sum(inv.amount_due for inv in tenant.invoices.all())
    total_payments = sum(p.amount for p in tenant.payments.all())
    account.balance = total_payments - total_invoices
    account.save()


# ---- SIGNAL HOOKS ----
@receiver(post_save, sender=Payment)
def update_balance_on_payment_save(sender, instance, **kwargs):
    recalc_tenant_account(instance.tenant)

@receiver(post_delete, sender=Payment)
def update_balance_on_payment_delete(sender, instance, **kwargs):
    recalc_tenant_account(instance.tenant)

@receiver(post_delete, sender=Invoice)
def update_balance_on_invoice_delete(sender, instance, **kwargs):
    recalc_tenant_account(instance.tenant)
