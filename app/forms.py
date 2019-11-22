from django import forms
from app.models import Students
from django.contrib.auth.models import User
from django.core import validators

class User_Form(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('username',"email",'password')
        
class Students_form(forms.ModelForm):
    #Phno=forms.CharField(required=True,max_length=10,min_length=10,\
       # validators=[validators.RegexValidator('[6-9]\d{9}')])
    class Meta:
        model=Students
        fields=('name','college',"profile_pic")