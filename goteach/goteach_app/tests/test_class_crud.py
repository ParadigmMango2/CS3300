from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Hosttest(LiveServerTestCase):
	example_title = "Example Title"
	example_date = "2024-04-14"

	def test010CreateClass(self):
		driver = webdriver.Firefox()
                                                                           
		driver.get('http://127.0.0.1:8000/')                                     
                                                                                   
		# Navigate to class list page
		# driver.find_elements("xpath", '//*[@class="class-list-button"]').click()
		driver.find_element(By.ID, "class-list-button").click()          
		assert "/classes/" in driver.current_url 

		# Navigate to class creation page
		driver.find_element(By.ID, "create-class-button").click()          
		assert "/classes/create_class/" in driver.current_url 
	
		# Insert fields and submit	
		driver.find_element(By.ID, "id_title").send_keys(self.example_title)          
		driver.find_element(By.ID, "id_start_date").send_keys(self.example_date)          
		submit_button = driver.find_element(By.ID, "submit-new-class-button")          
		#WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.ID, 'submit-new-class-button')))
		#submit_button.click()
		driver.execute_script("arguments[0].click();", submit_button) # Manually click the button with JS

		# Check that example class has been created
		example_title_xpath = '//h5[@class="class-title" and text()="{}"]'.format(self.example_title)
		WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, example_title_xpath)))
		assert len(driver.find_elements(By.XPATH, example_title_xpath)) > 0
