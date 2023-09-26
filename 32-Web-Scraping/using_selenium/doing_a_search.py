"""
USING SELENIUM MODULE: DOING A SEARCH


"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# CONSTANTS:
DRIVER_PATH = "C:\webdriver\chromedriver.exe"
TARGET_URL = "https://www.wikipedia.org/"
# Do not close the browser after actions:
browser_options = Options()
browser_options.add_experimental_option("detach", True)
# Defining the local browser service:
service = Service(executable_path=DRIVER_PATH)
# Configuring which browser will be used:
driver = webdriver.Chrome(service=service, options=browser_options)
# What website will be scrapped:
driver.get(TARGET_URL)
# Step 1/2 > Executing a searching:
input_search = driver.find_element(By.NAME, "search")
input_search.send_keys("python")
input_search.send_keys(Keys.ENTER)  # or, if it's a form, you can submit with input_search.submit()
# Step 2/2 > Find out the specific matter, and click on it:
link_to_click = driver.find_element(By.PARTIAL_LINK_TEXT, "language")
link_to_click.click()
