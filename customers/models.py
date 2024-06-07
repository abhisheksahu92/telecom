from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField(unique=True)
    adhar_number = models.CharField(max_length=12, unique=True)
    registration_date = models.DateField(auto_now_add=True)
    assigned_mobile_number = models.CharField(max_length=10, unique=True)
