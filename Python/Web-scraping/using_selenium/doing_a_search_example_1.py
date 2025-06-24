"""
USING SELENIUM MODULE: DOING A SEARCH
https://selenium-python.readthedocs.io/getting-started.html

"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Constants:
# DRIVER_PATH = "C:\webdriver\chromedriver.exe"
TARGET_URL = "https://www.wikipedia.org/"

# Custom browser options:
browser_opts = Options()
browser_opts.add_experimental_option("detach", True)  # Prevent the browser to get closed after actions.
# browser_opts.add_argument('--headless')  # Let's hide the browser when the script runs.

# Custom services:
# service = Service(executable_path=DRIVER_PATH)  # Defining the local browser service.

# Configuring which browser will be used:
# browser = webdriver.Chrome(service=service, options=browser_options)
browser = webdriver.Chrome(options=browser_opts)  # Edge(), Firefox()
# WebDriver will wait until the page has fully loaded (that is, the “onload” event has fired) before returning control
# to your test or script. Be aware that if your page uses a lot of AJAX on load then WebDriver may not know when it has
# completely loaded:
browser.get(TARGET_URL)

# Step 1/2 > Executing a searching:
elem = browser.find_element(By.NAME, "search")
elem.send_keys("python")
# Press Enter:
elem.send_keys(Keys.ENTER)  # or, if it's a form, you can submit with input_search.submit()

# Step 2/2 > Find out the specific matter, and click on it:
link_to_click = browser.find_element(By.PARTIAL_LINK_TEXT, "language")
link_to_click.click()

# browser.close()  # close the browser tab
# browser.quit()  # close the entire browser and close the webdriver.
