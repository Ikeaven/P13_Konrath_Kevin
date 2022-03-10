from django.test import TestCase, Client
from django.urls import reverse


def test_dummy():
    assert 1


class OC_lettings_site_Test(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("<h1>Welcome to Holiday Homes</h1>", str(response.content))