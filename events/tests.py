from django.test import TestCase


class MainPageIntegrationTest(TestCase):
    def test_main_page_returns_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
