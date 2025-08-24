from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
# Each tenant gets an account
class TenantAccount(models.Model):
    tenant = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, 
        blank=True,
        related_name='account'
    )
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Account for {self.tenant.username} - Balance {self.balance}"
    
# Monthly Rent Invoice
class Invoice(models.Model):
    tenant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, 
        blank=True,
        related_name='invoices'
    )
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, 
        choices=[('unpaid', 'Unpaid'), ('partial', 'Partially Paid')], 
        default='unpaid')
    
    def __str__(self):
        return f"Invoice {self.id} for {self.tenant.username} - {self.status}"
    
# Payment Record
class Payment(models.Model):
    tenant = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL,
        null=True, 
        blank=True,
        related_name="payments"
    )

    invoice = models.ForeignKey(
        Invoice, 
        on_delete=models.CASCADE,
        related_name="payments"
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)
    method = models.CharField(
        max_length=50,
        choices=[
            ("cash", "Cash"),
            ("bank", "Bank Transfer"),
            ("mpesa", "M-Pesa"),
        ],
        default="cash"
    )

    def __str__(self):
        return f"{self.tenant.username} {self.amount} ({self.method})"