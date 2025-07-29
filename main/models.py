from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Apartment(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.address})"
    
    class Meta:
        verbose_name_plural = "Apartments"

class Bedsitter(models.Model):
    apartment = models.ForeignKey(Apartment, related_name='bedsitters', on_delete=models.CASCADE)
    number = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.apartment.name} - Room {self.number}"
    
    class Meta:
        verbose_name_plural = "Bedsitters"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bedsitter = models.OneToOneField(Bedsitter, on_delete=models.SET_NULL, null=True, blank=True, related_name='tenant')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    id_number = models.CharField(max_length=20, blank=True, null=True)
    profile_photo = models.ImageField(upload_to='uploads/product', blank=True, null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

    