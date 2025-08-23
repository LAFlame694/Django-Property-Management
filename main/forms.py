from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Bedsitter

"""class AssignTenantForm(forms.Form):
    bedsitter = forms.ModelChoiceField(
        queryset = Bedsitter.objects.all(),
        label = "Select Bedsitter",
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    tenant = forms.ModelChoiceField(
        queryset = Profile.objects.filter(bedsitter__isnull=True),
        label = "Select Tenant",
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    def __init__(self, *args, **kwargs):
        initial_bedsitter = kwargs.pop('initial_bedsitter', None)
        super().__init__(*args, **kwargs)
        if initial_bedsitter:
            self.fields['bedsitter'].initial = initial_bedsitter.id"""

class TenantDetailsForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "first_name", 
            "phone_number", 
            "email", 
            "id_number",
            "bedsitter"
        ]
        labels = {
            "first_name": "Name",
            "phone_number": "Phone Number",
            "email": "Email",
            "id_number": "ID Number",
            "bedsitter": "Bedsitter",
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'id_number': forms.NumberInput(attrs={'class': 'form-control'}),
            "bedsitter": forms.Select(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make bedsitter field read-only but still keep its value on save
        self.fields["bedsitter"].disabled = True

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'})
    )

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        }

class TenantForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label="Select User",
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )
    
    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}), required=True)
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}), required=True)
    phone_number = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number'}), required=True)
    email = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}), required=True)
    id_number = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'ID Number'}), required=True)

    class Meta:
        model = Profile
        fields = ['user', 'first_name', 'last_name', 'phone_number', 'email', 'id_number']
