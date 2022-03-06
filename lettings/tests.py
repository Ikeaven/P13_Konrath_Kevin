from django.test import TestCase, Client
from django.urls import reverse

from lettings.models import Address, Letting


class Lettings_Test(TestCase):
    def setUp(self):
        address = Address.objects.create(
            number=11,
            street='rue du test',
            city='test_city',
            state='test_state',
            zip_code=434343,
            country_iso_code='fra'
        )
        Letting.objects.create(title='test', address=address)
        self.client = Client()

    def test_index(self):
        response = self.client.get(reverse("lettings_index"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("<h1>Lettings</h1>", str(response.content))

    def test_letting(self):
        response = self.client.get(reverse("letting", args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertIn("<h1>test</h1>", str(response.content))
