from django.test import TestCase, Client
from django.urls import reverse
from django.conf import settings
import json

class StatusTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_info(self):
            response = self.client.get(reverse('info'))
            self.assertEqual(response.status_code, 200)
            content = json.loads(response.content)
            self.assertEqual(content, settings.APP_INFO)