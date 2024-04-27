
import os

from django.test import TestCase
from django.urls import resolve
from django.core.exceptions import ValidationError

from ..urls import *


class TestURLs(TestCase):
    def setUp(self):
        self.test_user = 1

    # Test index URL
    def test_index_url(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)
