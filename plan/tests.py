from rest_framework import status
from rest_framework.test import APITestCase
from .models import Plan
from django.urls import reverse

# Create your tests here.

class PlanTests(APITestCase):
    def setUp(self):
        self.plan_data = {
            'name': 'Platinum365',
            'cost': 499,
            'validity': 365,
            'status': 'Active'
        }
        self.plan_data_post = {
            'name': 'Gold180',
            'cost': 299,
            'validity': 180,
            'status': 'Active'
        }

        self.plan = Plan.objects.create(**self.plan_data)

    def tearDown(self):
        Plan.objects.all().delete()

    def test_get_plans(self):
        url = reverse('plan-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_plan(self):
        url = reverse('plan-detail', args=[self.plan.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.plan.name)

    def test_update_plan(self):
        url = reverse('plan-detail', args=[self.plan.id])
        updated_data = self.plan_data.copy()
        updated_data['name'] = 'Gold180'
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_plan(self):
        url = reverse('plan-detail', args=[self.plan.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_create_plan(self):
        url = reverse('plan-list')
        response = self.client.post(url, self.plan_data_post, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Plan.objects.count(), 2)
