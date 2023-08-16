from django.db import models
from django import forms

# Create your models here.

class customer_profile(models.Model):
    UserName = models.CharField(max_length=20, blank=True,null=True)
    Email = models.EmailField(max_length=40, blank=True,null=True)
    Password = models.CharField(max_length=30, blank=True,null=True)
    ConfirmPassword = models.CharField(max_length=30, blank=True,null=True)
    SecurityCode = models.CharField(max_length=5,blank=True,null=True)


    

    def __str__(self):
        return str(self.UserName) 

