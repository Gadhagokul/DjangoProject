from django.db import models

# Create your models here.
class user1(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=12)
    password=models.CharField(max_length=50)
