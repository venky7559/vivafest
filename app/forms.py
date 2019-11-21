from django import forms
from app.models import Students
from django.contrib.auth.models import User


class User_Form(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('username',"email",'password')
        
class Students_form(forms.ModelForm):
    class Meta:
        model=Students
        fields=('name','college',"profile_pic")