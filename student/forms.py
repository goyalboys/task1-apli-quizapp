from django import forms
from . import models

class UserForm(forms.ModelForm):
    class Meta:
        model=models.student
        fields=["name",'email','password1','password2']