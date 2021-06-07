from django import forms
from . import models
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    class Meta:
        model=User()
        fields=['Name','email','password']