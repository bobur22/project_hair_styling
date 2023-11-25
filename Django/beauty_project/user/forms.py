from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

# from django.contrib.auth.models import User

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "placeholder": 'username'
    }))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        "placeholder": 'password'
    }))


class Registration(forms.ModelForm):
    confirm_password = forms.CharField(required=True, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "email", "password", "confirm_password")
        widgets = {
            'password': forms.PasswordInput()
        }

    def clean_confirm_password(self):
        if self.cleaned_data['confirm_password'] != self.cleaned_data['password']:
            raise ValidationError("Parollar bir xil emas !")
        return self.cleaned_data['confirm_password']
