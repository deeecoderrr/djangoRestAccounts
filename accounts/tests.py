from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token


class AccountTest(APITestCase):
    def setUp(self):
        self.test_user = User.objects.create_user('deecoderr', 'deecoderr@gmail.com'
                                                  )
        self.test_user.set_password('Abc@123')
        self.create_url = reverse('account-create')

    def test_create_user(self):
        data = {
            'username': 'abc',
            'email': 'hrsht123@gmail.com',
            'password': 'Pass@1234'
        }

        response = self.client.post(self.create_url, data, format='json')
        user = User.objects.latest('id')
        token = Token.objects.get(user=user)
        print(token)
        #self.assertEqual(response.data['token'], token.key)

        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['username'], data['username'])
        self.assertFalse('password' in response.data)
