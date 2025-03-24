# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class UserRegistrationForm(UserCreationForm):
    country = forms.CharField(max_length=100, required=False)
    region = forms.CharField(max_length=100, required=False)
    city = forms.CharField(max_length=100, required=False)
    street = forms.CharField(max_length=100, required=False)
    house_number = forms.CharField(max_length=10, required=False)
    postal_code = forms.CharField(max_length=10, required=False)
    phone_number = forms.CharField(max_length=20, required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 
                  'first_name', 'last_name', 'country', 'region', 'city', 
                  'street', 'house_number', 'postal_code', 'phone_number')