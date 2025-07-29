from django.shortcuts import render
from .models import Profile, Apartment, Bedsitter

# Create your views here.
def home(request):
    apartments = Apartment.objects.count()
    bedsitters = Bedsitter.objects.count()
    tenants = Profile.objects.count()
    return render(request, 'main/base.html', 
                  {"apartments": apartments, 
                   "bedsitters": bedsitters, 
                   "tenants": tenants,
                   })
