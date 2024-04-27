import os

from django.test import TestCase
from django.contrib.auth.models import Group
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
            'start_date':'2022-06-22',
            'about':'HEHEHEHEHEH nah',
            'ended':False,
            'game_link':'http://tygem.fuseki.info/game.php?id=45F29SL0'
        })

        self.assertTrue(form.is_valid())


    def test_user_form(self):
        # Create a teachers group queryset object for validation
        teachers_group = Group.objects.filter(name='Teachers')

        form = CreateUserForm(data={
            'username':'Username12',
            'password1':'2022-06-22Df!',
            'password2':'2022-06-22Df!',
            'groups':teachers_group
        })

        self.assertTrue(form.is_valid())
