from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Customer

class CustomerTests(APITestCase):
    def setUp(self):
        self.customer_data = {
            'name': 'Atul Yadav',
            'dob': '1990-01-01',
            'email': 'atul.yadav@gmail.com',
            'adhar_number': '123456789013',
            'assigned_mobile_number': '9876543211'
        }
        self.customer_data_post = {
            'name': 'Abhishek Sahu',
            'dob': '1993-01-01',
            'email': 'abhishek.sahu@gmail.com',
            'adhar_number': '123456789015',
            'assigned_mobile_number': '9876543213'
        }
        self.customer = Customer.objects.create(**self.customer_data)

    def tearDown(self):
        Customer.objects.all().delete()

    def test_get_customers(self):
        url = reverse('customer-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_customer(self):
        url = reverse('customer-detail', args=[self.customer.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.customer.name)

    def test_update_customer(self):
        url = reverse('customer-detail', args=[self.customer.id])
        updated_data = self.customer_data.copy()
        updated_data['name'] = 'Jane Doe'
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.customer.refresh_from_db()
        self.assertEqual(self.customer.name, 'Jane Doe')

    def test_delete_customer(self):
        url = reverse('customer-detail', args=[self.customer.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Customer.objects.count(), 0)

    def test_create_customer(self):
        url = reverse('customer-list')
        response = self.client.post(url, self.customer_data_post, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 2)


