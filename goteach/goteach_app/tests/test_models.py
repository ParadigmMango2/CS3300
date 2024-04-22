from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ..models import *


class TestModels(TestCase):
    def setUp(self):
        self.class_obj = Class.objects.create(
            title = "Example Title",
            start_date = "2024-04-12",
            pk = 42
        )
        
    # def test
