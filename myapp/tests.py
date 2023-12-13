from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from PIL import Image
from io import BytesIO

class MyAppTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)

    # Test User Authentication
    def test_user_login(self):
        url = reverse('login')
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
        self.assertIn('user_id', response.data)

    def test_user_registration(self):
        url = reverse('register')
        data = {'username': 'newuser', 'password': 'newpassword'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)
        self.assertIn('user_id', response.data)

    # Test CRUD Operations
    def test_crud_operations(self):
        url = reverse('crud_operations')
        
        # Test GET request
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test POST request
        data = {'field1': 'value1', 'field2': 'value2'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Test Text Completion
    def test_text_completion(self):
        url = reverse('api_3')
        data = {'title': 'Product Title'}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('description', response.data)
        self.assertIn('keywords', response.data)

    # Test Image Recognition
    def test_image_recognition(self):
        url = reverse('api_4')

        # Create a sample image for testing
        image = Image.new('RGB', (100, 100))
        image_io = BytesIO()
        image.save(image_io, format='JPEG')
        image_io.seek(0)

        data = {'image': image_io}

        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('keywords', response.data)
