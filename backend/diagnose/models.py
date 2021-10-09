from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Social Page Models

class blood_bank(models.Model):
    group = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    email = models.CharField(max_length=200)

class donations(models.Model):
    name = models.CharField(max_length=200)
    disease = models.CharField(max_length=200)
    ammount = models.CharField(max_length=200)
    prescription = models.ImageField()

class request_blood(models.Model):
    requester = models.ForeignKey(User,on_delete=models.CASCADE)
    unit = models.IntegerField()
    prescription = models.ImageField()

class blood_donate(models.Model):
    donor = models.ForeignKey(User,on_delete=models.CASCADE)
    location = models.CharField(max_length=300)
    date = models.DateField()

