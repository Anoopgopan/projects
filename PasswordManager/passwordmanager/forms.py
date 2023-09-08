from django import forms
from . models import UserRegistration

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        app_label = 'passwordmanager'
        model = UserRegistration
        fields = ['username','password']