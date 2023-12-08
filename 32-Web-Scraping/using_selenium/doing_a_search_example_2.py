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
TARGET_URL = "https://www.python.org"

# Custom browser options:
browser_opts = Options()
browser_opts.add_experimental_option("detach", True)  # Prevent the browser to get closed after actions.
# browser_opts.add_argument('--headless')  # Let's hide the browser when the script runs.

# Custom services:
# service = Service(executable_path=DRIVER_PATH)  # Defining the local browser service.

# Configuring which browser will be used:
# driver = webdriver.Chrome(service=service, options=browser_opts)
driver = webdriver.Chrome(options=browser_opts)  # Edge(), Firefox()
# WebDriver will wait until the page has fully loaded (that is, the “onload” event has fired) before returning control
# to your test or script. Be aware that if your page uses a lot of AJAX on load then WebDriver may not know when it has
# completely loaded:
driver.get(TARGET_URL)

# It's an assertion to confirm that title has the word “Python” in it:
assert "Python" in driver.title
# Step 1/2 > Executing a searching:
elem = driver.find_element(By.NAME, 'q')
# Making sure that, if some text is on the field, it will be removed:
elem.clear()
elem.send_keys("pycon")
# Press Enter:
elem.send_keys(Keys.RETURN)
# After submission of the page, you should get the result if there is any. To ensure that some results are found,
# make an assertion:
assert "No results found." not in driver.page_source

# driver.close()  # close the browser tab
# driver.quit()  # close the entire browser and close the webdriver.
