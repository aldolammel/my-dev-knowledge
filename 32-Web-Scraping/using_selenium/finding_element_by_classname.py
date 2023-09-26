"""
USING SELENIUM MODULE: BY CSS CLASS NAME

"""

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

# Defining the local browser service:
service = Service(executable_path="C:\webdriver\msedgedriver")
# Configuring which browser will be used:
driver = webdriver.Edge(service=service)
# What website will be scrapped:
driver.get("https://www.amazon.com.br/gp/product/B086Y75MF9")

price_currency = driver.find_element(By.CLASS_NAME, "a-price-symbol").text
price_value = driver.find_element(By.CLASS_NAME, "a-price-whole").text
price_fraction = driver.find_element(By.CLASS_NAME, "a-price-fraction").text

print(f"{price_currency}{price_value},{price_fraction}")

# driver.close()  # close the browser tab
driver.quit()  # close the entire browser and close the webdriver.
