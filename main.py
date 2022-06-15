# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from selenium import webdriver

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import wget

options = webdriver.ChromeOptions()
options.add_argument('-headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.google.com")

search_input = "gomycode formation"
search = driver.find_element(By.NAME, 'q')
search.send_keys(search_input)
search.send_keys(Keys.RETURN)

data = []

# Crawler
soup = BeautifulSoup(driver.page_source, 'html.parser')
content = soup.prettify()

for result in soup.select('.tF2Cxc'):
    title = result.select_one('.DKV0Md').text
    link = result.select_one('.yuRUbf a')['href']
    description = result.select_one('#rso .lyLwlc').text

    data.append({
         'title': title,
          'lien': link,
         'description':description,
    })


print(data)


#Next
def
search = driver.find_element(By.ID, 'pnnext')
search.send_keys(Keys.RETURN)
soup = BeautifulSoup(driver.page_source, 'html.parser')

for result in soup.select('.tF2Cxc'):
    title = result.select_one('.DKV0Md').text
    link = result.select_one('.yuRUbf a')['href']
    description = result.select_one('#rso .lyLwlc').text

    data.append({
         'title': title,
          'lien': link,
         'description':description,
    })