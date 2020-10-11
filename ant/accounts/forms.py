
from django import forms
from .models import User

class UserSignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'name','account']

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields =( 'username', 'password')
