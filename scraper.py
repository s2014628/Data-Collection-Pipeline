from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class Scraper:
    def __init__(self,url):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(url)
    def get_driver(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(url)
    def accept_cookies(self, xpath:str='//div[@class="banner-actions-container"]'):
        accept_cookies=self.driver.find_element(By.XPATH,value=xpath)
        accept_cookies.click()
    def browse_button(self,xpath:str='//*[@id="browseShopContainer"]/div/a/span'):
        browse_button=self.driver.find_element(By.XPATH,value=xpath)
        browse_button.click()
    def search_bar(self,
                    xpath:str='//input[@id="search"]',
                    product_category:str='meat'):
        search_bar=self.driver.find_element(By.XPATH,value=xpath)
        search_bar.click()
        self.driver.implicitly_wait(1)
        search_bar.send_keys(product_category)
        search_bar.send_keys(Keys.ENTER)
    def find_product(self,
                    container:str='//ul[@class="fops fops-regular fops-shelf"]',
                    tag:str='./li') -> list:
        container=self.driver.find_element(By.XPATH,value=container)
        products=container.find_elements(By.XPATH,value=tag)
        print(products)
        return products









