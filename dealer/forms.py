from django import forms
from .models import Sale
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['customer', 'total_price', 'car']


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password1', 'password2']


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password1', 'password2']
