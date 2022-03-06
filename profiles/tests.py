from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Profile


class Profile_Test(TestCase):
    def setUp(self):
        user = User.objects.create(
            username='test',
            password='test'
        )
        Profile.objects.create(user=user, favorite_city='city_test')
        self.client = Client()

    def test_index(self):
        response = self.client.get(reverse("profiles_index"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("<h1>Profiles</h1>", str(response.content))

    def test_letting(self):
        response = self.client.get(reverse("profile", args=['test']))
        self.assertEqual(response.status_code, 200)
        self.assertIn("<h1>test</h1>", str(response.content))
