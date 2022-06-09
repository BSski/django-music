from django.test import TestCase
from django.urls import reverse


class ViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.home_url = reverse("home")

    def test_can_see_home_view(self):
        response = self.client.get(self.home_url, secure=True)
        self.assertEqual(response.status_code, 200)
