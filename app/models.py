from django.db import models
#from app import forms
from django.contrib.auth.models import User

# Create your models here.
class Students(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE, default="")
    name=models.CharField(max_length=40)
    college=models.CharField(max_length=40)
    profile_pic=models.ImageField(upload_to='user',blank=True)

    def __str__(self):
        return self.user.username
