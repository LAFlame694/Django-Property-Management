from django.contrib import admin
from .models import TenantAccount, Invoice, Payment
from django.db.models import Sum

# Register your models here.
@admin.register(TenantAccount)
class TenantAccountAdmin(admin.ModelAdmin):
    list_display = ("tenant", "balance")

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ("tenant", "amount_due", "due_date", "status", "created_at", "total_paid", "outstanding")
    list_filter = ("status", "due_date")
    search_fields = ("tenant__username",)
    readonly_fields = ("status",)  # 👈 prevent manual edits

    def total_paid(self, obj):
        return obj.payments.aggregate(total=Sum('amount'))['total'] or 0.00
    
    def outstanding(self, obj):
        return (obj.amount_due or 0) - (self.total_paid(obj) or 0)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("tenant", "invoice", "amount", "method", "date")
    list_filter = ("method", "date")
    search_fields = ("tenant__username",)
