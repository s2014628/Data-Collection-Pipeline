from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
class Scraper:
    def __init__(self,url:str='https://www.ocado.com/'):
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
        self.driver.implicitly_wait(1)
    def find_product(self,
                    container:str='//ul[@class="fops fops-regular fops-shelf"]',
                    tag:str='./li') :
        self.driver.implicitly_wait(1)
        container=self.driver.find_element(By.XPATH,value=container)
        products=container.find_elements(By.XPATH,value=tag)
        time.sleep(1)
        return products
    def find_all_products(self):
        self.accept_cookies()
        self.driver.implicitly_wait(1)
        self.browse_button()
        self.driver.implicitly_wait(1)
        self.search_bar()
        self.driver.implicitly_wait(1)
        food_products=self.find_product()
        return food_products
    


# class PaddleScraper (Scraper):

    # def find_all_products(self):
    #     self.accept_cookies()
    #     time.sleep(1)
    #     self.browse_button()
    #     time.sleep(1)
    #     self.search_bar()
    #     time.sleep(1)
    #     food_products=self.find_product()
    #     # links=[]
    #     # a=food_products[0].find_element(By.XPATH,value='//a').get_attribute('href')
    #     # links.append(a)
    #     return food_products
    #     # for product in food_products:
    #     #     link=product.find_element(By.XPATH,value='//a').get_attribute('href')
    #     #     links.append(link)
    #     # return links
        





        

    









