from rest_framework import status
from rest_framework.test import APITestCase
from customers.models import Customer
from plan.models import Plan
from .models import CustomerPlan
from django.urls import reverse

# Create your tests here.
class CustomerPlanTests(APITestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            name='Abhishek Sahu',
            dob='1993-01-01',
            email='abhishek.sahu@gmail.com',
            adhar_number='123456789013',
            assigned_mobile_number='9876543213'
        )
        self.customer = Customer.objects.create(
            name='Abhishek Sahu',
            dob='1993-01-01',
            email='abhishek.sahu@gmail.com',
            adhar_number='123456789013',
            assigned_mobile_number='9876543213'
        )
        self.plan = Plan.objects.create(
            name='Platinum365',
            cost=499,
            validity=365,
            status='Active'
        )
        self.plan_gold = Plan.objects.create(
            name='Gold180',
            cost=299,
            validity=180,
            status='Active'
        )
        self.customer_plan_data = {
            'customer': self.customer.id,
            'plan': self.plan.id
        }
        self.customer_plan = CustomerPlan.objects.create(
            customer=self.customer,
            plan=self.plan,
            renewal_date='2024-07-30',
            existing_plan_name='Platinum365',
            new_plan_name='Gold180',
            plan_status='Active'
        )

    def tearDown(self):
        CustomerPlan.objects.all().delete()
        Customer.objects.all().delete()
        Plan.objects.all().delete()

    def test_create_customer_plan(self):
        url = reverse('customerplan-list')
        response = self.client.post(url, self.customer_plan_data, format='json')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomerPlan.objects.count(), 2)

    def test_get_customer_plans(self):
        url = reverse('customerplan-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_customer_plan(self):
        url = reverse('customerplan-detail', args=[self.customer_plan.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['existing_plan_name'], self.customer_plan.existing_plan_name)

    def test_update_customer_plan(self):
        url = reverse('customerplan-detail', args=[self.customer_plan.id])
        updated_data = {}
        updated_data['plan'] = self.plan_gold.id
        response = self.client.patch(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.customer_plan.refresh_from_db()
        self.assertEqual(self.customer_plan.new_plan_name, self.plan_gold.name)

    def test_delete_customer_plan(self):
        url = reverse('customerplan-detail', args=[self.customer_plan.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(CustomerPlan.objects.count(), 0)
