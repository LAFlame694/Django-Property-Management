from django.urls import path
from .views import mpesa_confirmation

urlpatterns = [
    path('confirm/', mpesa_confirmation, name='mpesa_confirmation'),
]