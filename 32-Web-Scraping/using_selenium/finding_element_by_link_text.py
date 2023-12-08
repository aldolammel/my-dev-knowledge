"""
USING SELENIUM MODULE: BY CSS LINK TEXT
https://selenium-python.readthedocs.io/getting-started.html

"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Constants:
# DRIVER_PATH = "C:\webdriver\chromedriver.exe"
TARGET_URL = "https://www.wikipedia.org/"

# Custom browser options:
browser_opts = Options()
browser_opts.add_experimental_option("detach", True)  # Do not close the browser after actions.
# browser_opts.add_argument('--headless')  # Let's hide the browser when the script runs.

# Custom services:
# service = Service(executable_path=DRIVER_PATH)  # Defining the local browser service.

# Configuring which browser will be used:
# driver = webdriver.Chrome(service=service, options=browser_opts)
driver = webdriver.Chrome(options=browser_opts)
# WebDriver will wait until the page has fully loaded (that is, the “onload” event has fired) before returning control
# to your test or script. Be aware that if your page uses a lot of AJAX on load then WebDriver may not know when it has
# completely loaded:
driver.get(TARGET_URL)

# Clicking:
link_to_click = driver.find_element(By.LINK_TEXT, "You can support our work with a donation.")
link_to_click.click()

# driver.close()  # close the browser tab
# driver.quit()  # close the entire browser and close the webdriver.
