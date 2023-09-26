"""
USING SELENIUM MODULE: CSS SELECTOR


"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# CONSTANTS:
DRIVER_PATH = "C:\webdriver\chromedriver.exe"
TARGET_URL = "https://python.org"
# Defining the local browser service:
service = Service(executable_path=DRIVER_PATH)
# Configuring which browser will be used:
driver = webdriver.Chrome(service=service)
# What website will be scrapped:
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
driver.quit()  # close the entire browser and close the webdriver.
