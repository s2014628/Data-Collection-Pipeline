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
import uuid



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
        prduct_price=self.driver.find_element(by=By.XPATH,value='//h2[@class="bop-price__current " ]').text
        return prduct_price


    def get_product_description(self):
        product_description=self.driver.find_element(by=By.XPATH,value='//div[@class="bop-info__content"]').text
        return product_description

    def get_uuid(self):
        '''Generates a random Universally Unique ID (UUID) for each property and appends to the dictionary
        '''
        uni_uid = str(uuid.uuid4())
        return uni_uid
    
    def get_img_link(self):
        img_tag=self.driver.find_element(by=By.XPATH,value='//img[@role="presentation"]')
        img_tag=img_tag.get_attribute('src')
        return img_tag
    
    def get_in_dictionary()
    
 
        










