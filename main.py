import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_driver_path = r"C:/SeleniumDrivers/chromedriver.exe"
service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get('https://www.insiderscreener.com/en/explore/au')


time.sleep(5)  

soup = BeautifulSoup(driver.page_source, 'html.parser')


table = soup.find('table')  
rows = table.find_all('tr')  

data = []
header = [th.text.strip() for th in rows[0].find_all('th')]

for row in rows[1:]: 
    values = [td.text.strip() for td in row.find_all('td')]
    row_data = dict(zip(header, values))
    data.append(row_data)

with open('output.json', mode='w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

driver.quit()
