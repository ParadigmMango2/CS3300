from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .scripts import login_as_teacher


class Hosttest(LiveServerTestCase):
	def test010Homepage(self):
		driver = webdriver.Firefox()

		driver.get(self.live_server_url)
		assert "GoTeach Homepage" in driver.title

		driver.quit()

	def test020ClassNav(self):
		driver = webdriver.Firefox()

		driver.get(self.live_server_url)
		
		# driver.find_elements("xpath", '//*[@class="class-list-button"]').click()
		driver.find_element(By.ID, "class-list-button").click()
		
		assert "/classes/" in driver.current_url

		driver.quit()


	def test030AboutNav(self):
		driver = webdriver.Firefox()
		driver.get(self.live_server_url)
		
		# About page navigation
		# driver.find_elements("xpath", '//*[@class="class-list-button"]').click()
		driver.find_element(By.ID, "about-nav-button").click()
		assert "/about/" in driver.current_url

		driver.quit()


	def test040Login(self):
		driver = webdriver.Firefox()
		driver.get(self.live_server_url)

		# Login
		login_as_teacher(driver, self.live_server_url)

		# Verify login
		assert len(driver.find_elements(By.ID, "logout-nav-button")) > 0

		driver.quit()


	def test050Logout(self):
		driver = webdriver.Firefox()
		driver.get(self.live_server_url)

		# Login
		login_as_teacher(driver, self.live_server_url)
		assert len(driver.find_elements(By.ID, "logout-nav-button")) > 0

		# Logout
		driver.find_element(By.ID, "logout-nav-button").click()
		assert "/logout/" in driver.current_url

		driver.quit()

