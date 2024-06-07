# customerplan/tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import CustomerPlan
from customers.models import Customer
from plan.models import Plan
from datetime import datetime

class PlanRenewalViewTestCase(APITestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            name='Abhishek Sahu',
            dob='1993-01-01',
            email='abhishek.sahu@gmail.com',
            adhar_number='123456789013',
            assigned_mobile_number='9876543213'
        )
        self.plan = Plan.objects.create(
            name='Platinum365',
            cost=499.00,  # Ensure this is a decimal
            validity=365,
            status='Active'
        )
        self.customer_plan_data = {
            'customer': self.customer,
            'plan': self.plan,
            'existing_plan_expiry': '2024-06-30',
            'renewal_date': '2024-07-01',
            'existing_plan_name': 'Gold180',
            'new_plan_name': 'Platinum365',
            'plan_status': 'Active'
        }
        self.customer_plan = CustomerPlan.objects.create(**self.customer_plan_data)

    def test_renew_plan_successfully(self):
        url = reverse('renew-customer-plan', kwargs={'customer_plan_id': self.customer_plan.id})
        renew_data = {
            'renewal_date': '2025-07-01',
            'plan_status': 'Active'
        }
        response = self.client.post(url, renew_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(CustomerPlan.objects.get(id=self.customer_plan.id).renewal_date, datetime.strptime(renew_data['renewal_date'], '%Y-%m-%d').date())
        self.assertEqual(CustomerPlan.objects.get(id=self.customer_plan.id).plan_status, renew_data['plan_status'])

    def test_renew_plan_invalid_customer_plan_id(self):
        invalid_customer_plan_id = 9999
        url = reverse('renew-customer-plan', kwargs={'customer_plan_id': invalid_customer_plan_id})
        renew_data = {
            'renewal_date': '2025-07-01',
            'plan_status': 'Active'
        }
        response = self.client.post(url, renew_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
