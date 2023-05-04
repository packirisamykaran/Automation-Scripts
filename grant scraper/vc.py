

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import openpyxl
import csv
# instantiate options
options = webdriver.ChromeOptions()

# run browser in headless mode
# options.headless = True

# instantiate driver
driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()), options=options)

# load website
url = 'https://airtable.com/shr6iB94YAZJ6P89R/tblMc5bwjZlIeeYLd?backgroundColor=blue&viewControls=on'

# get the entire website content
driver.get(url)


nameElement = driver.find_element(By.CLASS_NAME, 'dataLeftPaneInnerContent')


nameRows = driver.find_elements(By.CLASS_NAME, 'line-height-4')

for row in nameRows:
    print(row.text)
