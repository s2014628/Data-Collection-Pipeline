from multiprocessing.sharedctypes import Value
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import Chrome
!pip install webdriver-manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver=Chrome(ChromeDriverManager().install())
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



class scraper:
    def __init__(self,url,driver) :
        self.url=url
        self.driver=driver
        self.product_list={"Product_name":[],"weight":[],"price":[],"Description":[]}


    def accept_cookies(self):
        cookies_button=self.driver.find_element(by=By.XPATH,value='//*[@id="onetrust-accept-btn-handler"]')
        cookies_button.click()
        time.sleep(2)
        return self.driver
    

    def get_product_list(self):
        product_container=self.driver.find_element(by=By.XPATH,value='//*[@id="main-content"]/div[2]/div[2]/ul')
        product_list=product_container.find_elements(by=By.XPATH,value='./li')
        return product_list
    
    def get_product_name(self):
        tag_product_name=self.driver.find_element(by=By.CLASS_NAME ,value="bop-title")
        name=tag_product_name.find_element(by=By.XPATH,value='.//h1').text
        return name
    
    def get_product_weight(self):
        tag_product_weight=self.driver.find_element(by=By.CLASS_NAME ,value="bop-title")
        weight=tag_product_weight.find_element(by=By.XPATH,value='.//span[@class="bop-catchWeight"]').text
        return weight
    def get_product_price(self):
        get_prduct_price=self.driver.find_element(by=By.XPATH,value='//h2[@class="bop-price__current " ]').text
        return get_prduct_price
    







    
product_list=product_container.find_elements(by=By.XPATH,value='./li')
num_list=len(product_list)




