from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Hosttest(LiveServerTestCase):
	def test010Homepage(self):
		driver = webdriver.Firefox()

		driver.get('http://127.0.0.1:8000/')
		assert "GoTeach Homepage" in driver.title

	def test020ClassNav(self):
		driver = webdriver.Firefox()

		driver.get('http://127.0.0.1:8000/')
		
		# driver.find_elements("xpath", '//*[@class="class-list-button"]').click()
		driver.find_element(By.ID, "class-list-button").click()
		
		assert "/classes/" in driver.current_url

