"""
USING SELENIUM MODULE: DOING THE LOGGING


"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

# CONSTANTS:
DRIVER_PATH = "C:\webdriver\chromedriver.exe"
TARGET_URL = "https://web.archive.org/web/20220120120408/https://secure-retreat-92358.herokuapp.com/"
USERNAME = os.environ["USERNAME"]
USERLASTNAME = os.environ["USERLASTNAME"]
USEREMAIL = os.environ["USEREMAIL"]
# Do not close the browser after actions:
browser_options = Options()
browser_options.add_experimental_option("detach", True)
# Defining the local browser service:
service = Service(executable_path=DRIVER_PATH)
# Configuring which browser will be used:
driver = webdriver.Chrome(service=service, options=browser_options)
# What website will be scrapped:
driver.get(TARGET_URL)

# filling the form:
field_name = driver.find_element(By.NAME, "fName")
field_name.send_keys(USERNAME)

field_last_name = driver.find_element(By.NAME, "lName")
field_last_name.send_keys(USERLASTNAME)

field_email = driver.find_element(By.NAME, "email")
field_email.send_keys(USEREMAIL)

submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()
