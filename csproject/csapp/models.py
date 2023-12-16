from django.db import models


class User(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.EmailField()
    phoneno = models.CharField(max_length=15) 
    password=models.CharField(max_length=100)
    confirmpassword=models.CharField(max_length=100)