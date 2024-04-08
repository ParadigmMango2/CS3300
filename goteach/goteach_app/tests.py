from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By


class Hosttest(LiveServerTestCase):
	
	def testhomepage(self):
		driver = webdriver.Firefox()

		driver.get('http://127.0.0.1:8000/')
		assert "GoTeach Homepage" in driver.title

	def testX(self):
		driver = webdriver.Firefox()

		driver.get('http://127.0.0.1:8000/')
		
		# driver.find_elements("xpath", '//*[@class="class-list-button"]').click()
		driver.find_element(By.CLASS_NAME, "class-list-button").click()

		pass
		

