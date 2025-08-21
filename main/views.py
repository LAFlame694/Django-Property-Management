from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, Apartment, Bedsitter
from .forms import TenantForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, TenantDetailsForm

# Create your views here.
def about(request):
    return render(request, 'main/about.html')

def command_center(request):
    apartment = Apartment.objects.all()
    context = {'apartments': apartment,}
    return render(request, 'main/command_center.html', context)

def add_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User account created successfully.')
            return redirect('tenant_dashboard_admin')  # Change to your dashboard URL name
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'main/add_user.html', {'form': form})

def tenant_dashboard_admin(request):
    tenants = Profile.objects.all()
    context = {'tenants': tenants}
    return render(request, 'main/tenant_dashboard_admin.html', context)

def add_tenant(request):
    if request.method == 'POST':
        form = TenantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tenant_dashboard')  # redirect after saving
    else:
        form = TenantForm()

    return render(request, 'main/add_tenant.html', {'form': form})

def tenant_list(request):
    tenants = Profile.objects.all()
    return render(request, 'main/tenant_list.html', {"tenants": tenants})

def tenant_detail(request, tenant_id):
    tenant = get_object_or_404(Profile, id=tenant_id)

    if request.method == "POST":
        form = TenantDetailsForm(request.POST, request.FILES, instance=tenant)
        if form.is_valid():
            form.save()
            return redirect("tenant_detail", tenant_id=tenant.id)
    else:
        form = TenantDetailsForm(instance=tenant)

    context = {
        "tenant": tenant,
        "form": form,
    }
    return render(request, "main/tenant_detail.html", context)

def apartment_detail(request, apartment_id):
    apartment = get_object_or_404(Apartment, id=apartment_id)
    bedsitters = apartment.bedsitters.select_related('tenant').all()
    context = {
        'apartment': apartment,
        'bedsitters': bedsitters
        }
    return render(request, 'main/apartment_detail.html', context)

def apartment_dashboard(request):
    apartments = Apartment.objects.all()
    context = {"apartments": apartments}
    return render(request, "main/apartment_dashboard.html", context)

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