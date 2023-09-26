"""
USING SELENIUM MODULE: XPATH

XPATH = XPath stands for XML Path Language. It uses a non-XML syntax to provide a flexible way of addressing
(pointing to) different parts of an XML document. It can also be used to test addressed nodes within a document
to determine whether they match a pattern or not.

To find the XPath of an Element, use Chrome's built-in Developer Tools.
1) Right-click the web element in browser and select Inspect.
2) It will launch the Developer tool with highlighted Element's HTML code.
3) Copy Xpath by right-clicking the highlighted HTML.
4) Use the copied Xpath to locate this Element in browser later.

"""

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

# Defining the local browser service:
service = Service(executable_path="C:\webdriver\msedgedriver")
# Configuring which browser will be used:
driver = webdriver.Edge(service=service)
# What website will be scrapped:
driver.get("https://aldolammel.com/")

xpath_example = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[3]/div/div[2]/a")

print(xpath_example.text)  # it should result "Assistir 3ª temporada".


