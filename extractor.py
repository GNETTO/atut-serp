from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#import wget


class Driver:

    driver = ""

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('-headless')
        Driver.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

class Extractor:

    driver = ""

    def __init__(self, entries):
        self.driver = Driver().driver
        self.search_input = entries

    def lunch_driver(self):
        self.driver.get(f'https://www.google.com/search?={self.search_input}')

    def set_page_entry(self):
        search = self.driver.find_element(By.NAME, 'q')
        search.send_keys(self.search_input)
        search.send_keys(Keys.RETURN)

    def get_resoures(self):
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        # content = soup.prettify()
        data = []
        for result in soup.select('.tF2Cxc'):
            title = result.select_one('.DKV0Md').text
            link = result.select_one('.yuRUbf a')['href']
            description = result.select_one('#rso .lyLwlc')

            if result.find('div', class_="lyLwlc") == None:
                description = None
            else:
                description = description.text.strip()

            data.append({
                'title': title,
                'lien': link,
                'description': description,
            })

        return data

    def start_extraction(self):
        self.lunch_driver()
        self.set_page_entry()
        return self.get_resoures()

