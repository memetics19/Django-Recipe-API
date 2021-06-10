from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Ingredient

from recipe.serializers import IngredientSerializer

INGREDIENT_URL = reverse('recipe:ingredient-list')

class PublicIngredientsAPITests(TestCase):
    """Tests for publicly available ingredients API"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test login is required to access the ingredient"""
        res = self.client.get(INGREDIENT_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

class PrivateIngredientsAPITests(TestCase):
    """Test the private API"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'test@namaskar.in',
            'test@1233iii'
        )
        self.client.force_authenticate(self.user)

    def test_retrieve_ingredient_list(self):
        """Test retrieving a list of ingredients"""
        Ingredient.objects.create(user=self.user, name="wheat")
        Ingredient.objects.create(user=self.user, name = "broken")

        res = self.client.get(INGREDIENT_URL)


        ingredients = Ingredient.objects.all().order_by('name')
        serializer = IngredientSerializer(ingredients, many=True)
        self.assertEqual(res.data, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
    
    def test_ingredient_limited_to_user(self):
        """Test the tags returned for the authenticated user"""
        user2 = get_user_model().objects.create_user(
            'hello@namaskar.in',
            'testpassa123'
        )
        Ingredient.objects.create(user=user2, name ="vegetable")
        ingredient = Ingredient.objects.create(user = self.user, name= "test-food")

        res = self.client.get(INGREDIENT_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['name'],ingredient.name)

   