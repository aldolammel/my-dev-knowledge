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
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Constants:
# DRIVER_PATH = "C:\webdriver\chromedriver.exe"
TARGET_URL = "https://aldolammel.com/"

# Custom browser options:
browser_opts = Options()
# browser_opts.add_experimental_option("detach", True)  # Do not close the browser after actions.
browser_opts.add_argument('--headless')  # Let's hide the browser when the script runs.

# Custom services:
# service = Service(executable_path=DRIVER_PATH)  # Defining the local browser service.

# Configuring which browser will be used:
# driver = webdriver.Chrome(service=service, options=browser_opts)
driver = webdriver.Chrome(options=browser_opts)
# WebDriver will wait until the page has fully loaded (that is, the “onload” event has fired) before returning control
# to your test or script. Be aware that if your page uses a lot of AJAX on load then WebDriver may not know when it has
# completely loaded:
driver.get(TARGET_URL)

# Searching the element and printing it out:
xpath_example = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[3]/div/div[2]/a")
print(xpath_example.text)  # it should result "Assistir 3ª temporada".

# driver.close()  # close the browser tab
# driver.quit()  # close the entire browser and close the webdriver.
