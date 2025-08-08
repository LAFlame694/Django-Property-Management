from . import views
from django.urls import path
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='main/login.html'), name='login'),
    path('', views.home, name='home'),
    path('tenant-dashboard/', views.tenant_dashboard, name='tenant_dashboard'),
    path('dashboard/', views.dashboard_redirect, name='dashboard_redirect'),
    path('manage-property/', views.manage_property, name='manage_property'),
]