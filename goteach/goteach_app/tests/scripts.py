from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def login_as_teacher(driver, live_server_url):
    test_username = 'TestTeacher'
    test_pwd = 'very=seKret23'

    # Create user
    User = get_user_model()
    # try:
    # 	User.objects.create_user(username=test_username, password=test_pwd)
    # except Exception as e:
    # 	print(f"Error creating user: {e}")
    user = User.objects.create_user(username=test_username, password=test_pwd)

    # Create teachers group and add user to it
    teachers_group = Group.objects.get_or_create(name='Teachers')
    teachers_group_id = Group.objects.get(name = 'Teachers')
    user.groups.add(teachers_group_id)

    # driver.get('http://127.0.0.1:8000/')                      
    driver.get(live_server_url)

    # Navigate to login page
    driver.find_element(By.ID, "login-nav-button").click()          
    assert "/login/" in driver.current_url 

    # Login
    driver.find_element(By.ID, "id_username").send_keys(test_username)          
    driver.find_element(By.ID, "id_password").send_keys(test_pwd)          
    driver.find_element(By.ID, "login-button").click()          
