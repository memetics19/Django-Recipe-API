from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('user:create')
TOKEN_URL = reverse('user:token')

def create_user(**params):
    return get_user_model().objects.create_user(**params)

class PublicUserApiTest(TestCase):
    """Test the user's API(Public)"""

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """Test creating user is successful"""
        payload = {
            'email':'test@namaskar.in',
            'password':'testpass',
            'name':'test'
        }
        res = self.client.post(CREATE_USER_URL,payload)

        self.assertEqual(res.status_code,status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password',res.data)

    def test_user_exists(self):
        """test created user already exists """

        payload = {'email':'test@namaskar.in','password':'test123'}
        create_user(**payload)

        res = self.client.post(CREATE_USER_URL,payload)

        self.assertEqual(res.status_code,status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """Test the password should be more than 8  password"""
        payload = {'email':'test@namaskar.in','password':'test123','name':'test'}
        res = self.client.post(CREATE_USER_URL,payload)


        self.assertEqual(res.status_code,status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email = payload['email']
        ).exists()
        self.assertFalse(user_exists)

    def test_create_token(self):
        """Test That creates a token for user"""
        payload = {
            'email':'test@namaskar.in',
            'password':'password@1'
        }
        create_user(**payload)
        res = self.client.post(TOKEN_URL,payload)

        self.assertIn('token',res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_token_invalid(self):
        """Test that is invalid token for user"""
        
        payload = {
            'email':'test@namaskar.in',
            'password':'wrong'
        }

        res = self.client.post(TOKEN_URL, payload)

        self.assertNotin('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
    

    def test_create_token_missing_field(self):
        """Test that email and password are required"""

        res = self.client.post(TOKEN_URL, {'email':'one','password':''})
        self.assertNotIn('token',res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    

