from rest_framework.test import APITestCase
from django.urls import reverse


class SuperUserCreateRoleTestcases(APITestCase):
    """Test for superuser Register API"""
    REGISTER_URL = reverse('accountio:create')

    def test_register_staff(self):
        """Test Register staff."""
        payload = {
            "username": "user1",
            "email": "user@gmail.com",
            "password": "123456789Aas",
            "password2": "123456789Aas"
        }

        response = self.client.post(self.REGISTER_URL, payload)
        print(response.data['serializer']['username'], 'jjjjjjjjjjjjjjjjjjjjjjjjjjj')

        response_data = {
            "username": response.data['serializer']['username'],
            "email": response.data['serializer']['email']

        }

        expected_data = {
            "username": "user1",
            "email": "user@gmail.com",

        }

        self.assertEqual(response.status_code, 201)
        self.assertEqual(expected_data, response_data)
