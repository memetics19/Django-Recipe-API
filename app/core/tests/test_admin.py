from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email = "admin@namaskar.in",
            password = "admin@123"
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email = "test@namaskar.com",
            password = "pass123",
            name = "Test user"
        )
    
    def test_users_listed(self):
        """Test where all the users are listed on the user page"""

        url  = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change',args = [self.user.id])
        # /admin/core/user/1
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test create user page"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)