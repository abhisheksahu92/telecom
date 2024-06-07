from django.db import models
from customers.models import Customer
from plan.models import Plan

class CustomerPlan(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    existing_plan_expiry = models.DateField(null=True, blank=True)  # Expiry date of the existing plan
    renewal_date = models.DateField(null=True, blank=True)
    existing_plan_name = models.CharField(max_length=50, null=True, blank=True)
    new_plan_name = models.CharField(max_length=50, null=True, blank=True)
    plan_status = models.CharField(max_length=10, choices=[('Active', 'Active'), ('Inactive', 'Inactive')],null=True)

