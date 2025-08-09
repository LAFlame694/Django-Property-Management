from . import views
from django.urls import path
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='main/login.html'), name='login'),
    path('', views.home, name='home'),
    path('tenant-dashboard/', views.tenant_dashboard, name='tenant_dashboard'),
    path('dashboard/', views.dashboard_redirect, name='dashboard_redirect'),
    path('manage-property/', views.manage_property, name='manage_property'),
    path('apartment_dashboard/', views.apartment_dashboard, name='apartment_dashboard'),
    path('<int:apartment_id>/', views.apartment_detail, name='apartment_detail'),
    path('tenant/<int:tenant_id>/', views.tenant_detail, name='tenant_detail'),
]