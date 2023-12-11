from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUser(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class CategoryForm(forms.Form):
    title = forms.CharField(max_length=100)
    details = forms.CharField(max_length=300)
