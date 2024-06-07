from django.db import models

class Plan(models.Model):
    PLANS = [
        ('Platinum365', 'Platinum365'),
        ('Gold180', 'Gold180'),
        ('Silver90', 'Silver90'),
    ]

    COST_CHOICES = [
        (499, 499),
        (299, 299),
        (199, 199),
    ]

    VALIDITY_CHOICES = [
        (365, 365),
        (180, 180),
        (90, 90),
    ]

    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]

    name = models.CharField(max_length=50, choices=PLANS, unique=True)
    cost = models.IntegerField(choices=COST_CHOICES)
    validity = models.IntegerField(choices=VALIDITY_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
