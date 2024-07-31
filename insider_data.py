import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import json

# Set up the WebDriver
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_driver_path = r"C:/SeleniumDrivers/chromedriver.exe"
service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to the NSE India stock page
url = f"https://www.insiderscreener.com/en/company/advance-zinctek-ltd"
driver.get(url)


