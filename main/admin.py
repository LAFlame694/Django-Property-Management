from django.contrib import admin
from .models import Apartment, Bedsitter, Profile

# Register your models here.
admin.site.register(Apartment)
admin.site.register(Bedsitter)
admin.site.register(Profile)
