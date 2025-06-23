"""
USING SELENIUM MODULE: DOING THE LOGGING
https://selenium-python.readthedocs.io/getting-started.html

"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

# Constants:
# DRIVER_PATH = "C:\webdriver\chromedriver.exe"
TARGET_URL = "https://aldolammel.com/loja/wp-admin"
PROTECTED_USER = os.environ["PROTECTED_USER"]
PROTECTED_PASS = os.environ["PROTECTED_PASS"]

# Custom browser options:
browser_opts = Options()
browser_opts.add_experimental_option("detach", True)  # Do not close the browser after actions.
# browser_opts.add_argument('--headless')  # Let's hide the browser when the script runs.

# Custom services:
# service = Service(executable_path=DRIVER_PATH)  # Defining the local browser service.

# Configuring which browser will be used:
# browser = webdriver.Chrome(service=service, options=browser_opts)
browser = webdriver.Chrome(options=browser_opts)
# WebDriver will wait until the page has fully loaded (that is, the “onload” event has fired) before returning control
# to your test or script. Be aware that if your page uses a lot of AJAX on load then WebDriver may not know when it has
# completely loaded:
browser.get(TARGET_URL)

# filling the form:
field_user = browser.find_element(By.NAME, "log")
field_user.send_keys(PROTECTED_USER)

field_pwd = browser.find_element(By.NAME, "pwd")
field_pwd.send_keys(PROTECTED_PASS)

submit = browser.find_element(By.NAME, "wp-submit")
submit.click()

# browser.close()  # close the browser tab
# browser.quit()  # close the entire browser and close the webdriver.
