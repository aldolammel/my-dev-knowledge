"""
USING SELENIUM MODULE: CSS SELECTOR
https://selenium-python.readthedocs.io/getting-started.html

"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Constants:
# DRIVER_PATH = "C:\webdriver\chromedriver.exe"
TARGET_URL = "https://python.org"

# Custom browser options:
browser_opts = Options()
browser_opts.add_experimental_option("detach", True)  # Prevent the browser to get closed after actions.
# browser_opts.add_argument('--headless')  # Let's hide the browser when the script runs.

# Custom services:
# service = Service(executable_path=DRIVER_PATH)  # Defining the local browser service.

# Configuring which browser will be used:
driver = webdriver.Chrome(options=browser_opts)
driver.get(TARGET_URL)

events = dict()
events_time = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
events_title = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

for i in range(len(events_time)):
    events[i] = {
        "time": events_time[i].text,
        "title": events_title[i].text
    }
    print(f"{events[i]['time']} - {events[i]['title']}")

# driver.close()  # close the browser tab
# driver.quit()  # close the entire browser and close the webdriver.
