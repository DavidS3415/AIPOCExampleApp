import pytest
import subprocess
import time
import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Fixture to set up the Selenium driver
@pytest.fixture(scope="module")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()

# Fixture to start a fresh live server instance
@pytest.fixture(scope="module")
def live_server():
    # Use the current Python interpreter from the virtual environment.
    env = os.environ.copy()
    server_process = subprocess.Popen([sys.executable, "./src/backend/server.py"], env=env)
    
    time.sleep(3)
    
    yield
    
    # Terminate the server after tests complete.
    server_process.terminate()

# Test that verifies the UI can submit a new user and that the user appears in the list.
def test_ui_add_user(driver, live_server):
    driver.get("http://127.0.0.1:5000/test")
    wait = WebDriverWait(driver, 10)
    
    # Locate form inputs and submit button
    name_input = driver.find_element(By.ID, "name")
    email_input = driver.find_element(By.ID, "email")
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    
    # Enter test data for a new user
    test_name = "Selenium Test"
    test_email = "selenium@test.com"
    name_input.clear()
    name_input.send_keys(test_name)
    email_input.clear()
    email_input.send_keys(test_email)
    submit_button.click()
    
    # Wait for the new user to appear in the list
    wait.until(EC.text_to_be_present_in_element((By.ID, "userList"), test_name))
    
    # Verify that the new user appears in the list
    user_list = driver.find_element(By.ID, "userList")
    items = user_list.find_elements(By.TAG_NAME, "li")
    user_found = any(test_name in item.text and test_email in item.text for item in items)
    assert user_found, "New user should appear in the user list after submission."
