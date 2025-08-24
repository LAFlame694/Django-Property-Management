from django.contrib import admin
from .models import TenantAccount, Invoice, Payment

# Register your models here.
@admin.register(TenantAccount)
class TenantAccountAdmin(admin.ModelAdmin):
    list_display = ("tenant", "balance")

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ("tenant", "amount_due", "due_date", "status", "created_at")
    list_filter = ("status", "due_date")
    search_fields = ("tenant__username",)  # ✅ note the comma

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("tenant", "invoice", "amount", "method", "date")
    list_filter = ("method", "date")
    search_fields = ("tenant__username",)  # ✅ fixed with a comma
