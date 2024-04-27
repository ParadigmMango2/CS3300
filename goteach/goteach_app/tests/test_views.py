
import os

from django.test import TestCase
from django.test import Client
from django.core.exceptions import ValidationError

from ..views import *


class TestViews(TestCase):
    def setUp(self):
        # Set up client and user data
        self.test_user = 1
        self.client = Client()
        self.user = User.objects.create_user(username='test_username', password='test_pwd23!')


    # Test index view
    def test_index_view(self):
        # Call the index view with a response
        response = self.client.get(reverse('index'))

        # Validate that the view is valid
        self.assertEquals(response.status_code, 200)

        # Validate that the index template was used
        self.assertTemplateUsed(response,'goteach_app/index.html')
