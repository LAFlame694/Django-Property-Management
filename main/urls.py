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
    path("tenants/", views.tenant_list, name="tenant_list"),
    path('<int:apartment_id>/', views.apartment_detail, name='apartment_detail'),
    path('tenant/<int:tenant_id>/', views.tenant_detail, name='tenant_detail'),
    path('tenant/add/', views.add_tenant, name='add_tenant'),
    path('tenant-dashboard-admin/', views.tenant_dashboard_admin, name='tenant_dashboard_admin'),
    path('add-user/', views.add_user, name='add_user'),
    path('command-center/', views.command_center, name='command_center'),
    path('about/', views.about, name='about'),
    path('edit/<int:id>/', views.edit, name='edit'),
]