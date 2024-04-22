import os

from django.test import TestCase
from django.core.exceptions import ValidationError

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ..forms import *


class TestForms(TestCase):
    def test_class_form(self):
        form = ClassForm(data={
            'title':'TestTitle12',
            'start_date':'2022-06-22'
        })

        self.assertTrue(form.is_valid())
