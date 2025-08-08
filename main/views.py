from django.shortcuts import render, redirect
from .models import Profile, Apartment, Bedsitter
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
def manage_property(reqeust):
    return render(reqeust, "main/manage_property.html", {})

def dashboard_redirect(request):
    if request.user.is_superuser or request.user.is_staff:
        return redirect('home')  # name of your home url
    else:
        return redirect('tenant_dashboard')  # name of your tenant dashboard url

def tenant_dashboard(request):
    return render(request, "main/tenant_dashboard.html", {})

@login_required
def home(request):
    apartments = Apartment.objects.count()
    bedsitters = Bedsitter.objects.count()
    tenants = Profile.objects.count()
    return render(request, 'main/home.html', 
                  {"apartments": apartments, 
                   "bedsitters": bedsitters, 
                   "tenants": tenants,
                   })