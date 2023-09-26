from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

# Do not close the browser after actions:
browser_options = Options()
browser_options.add_experimental_option("detach", True)
# Defining the local browser service:
service = Service(executable_path="C:\webdriver\msedgedriver")
# Configuring which browser will be used:
driver = webdriver.Edge(service=service, options=browser_options)
# What website will be scrapped:
driver.get("https://www.wikipedia.org/")
# Clicking:
link_to_click = driver.find_element(By.LINK_TEXT, "You can support our work with a donation.")
link_to_click.click()
