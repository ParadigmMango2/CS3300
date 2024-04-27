import os

from django.test import TestCase
from django.core.exceptions import ValidationError

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
            ended = False,
            about = "Something something, pun pun.",
            game_link = "https://youtu.be/hrXBc7hsK7I?si=bPIRqd_O6oPWZ4u2",
            pk = 42
        )
        

    def testClassPk(self):
        class_pk = str(self.class_obj.pk)
        # Join class pk in an absolute url.  The '' at the end adds the trailing slash.
        class_url = os.path.join('/classes/', class_pk, '')

        # print(self.class_obj.get_absolute_url())
        # print(class_url)

        self.assertEquals(class_url, self.class_obj.get_absolute_url())


    def testClassInstance(self):
        self.assertEquals(str(self.class_obj), 'Example Title')
        self.assertTrue(isinstance(self.class_obj, Class))
        
