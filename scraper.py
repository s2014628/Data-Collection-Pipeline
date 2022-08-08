from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import uuid
from uuid import uuid4
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
                    container:str='//*[@id="main-content"]/div[2]/div[3]/ul',
                    tag:str='./li') :
        self.accept_cookies()
        self.driver.implicitly_wait(1)
        self.browse_button()
        self.driver.implicitly_wait(1)
        self.search_bar()
        self.driver.implicitly_wait(1)
        container=self.driver.find_element(By.XPATH,value=container)
        products=container.find_elements(By.XPATH,value=tag)
        time.sleep(1)
        links=[]
        for product in products:
            find_all_div_under_li_class=product.find_elements(By.XPATH,value='./div')
            find_url_tag=find_all_div_under_li_class[1].find_element(By.XPATH,
                                                            value='//div[@class="fop-contentWrapper"]')
            link=find_url_tag.find_element(By.XPATH,value='//a').get_attribute('href')
            links.append(link)
        print(links)















    # def get_links(self):
    #     self.accept_cookies()
    #     self.driver.implicitly_wait(1)
    #     self.browse_button()
    #     self.driver.implicitly_wait(1)
    #     self.search_bar()
    #     self.driver.implicitly_wait(1)
    #     food_products=self.find_product()
    #     for food_product in food_products:
    #         self.driver.implicitly_wait(1)
    #         food_product.click()
    #         self.driver.implicitly_wait(1)

    #         self.driver.back()




            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
                    # each_uuid=str(uuid.uuid4())
            # uuid.append(each_uuid)
            # tag_data_sku=food_product.find_elements(By.XPATH,value='./div')
            # data_sku=tag_data_sku[1].get_attribute('data-sku')
            # unique_id.append(data_sku)
            # unique_id.append(food_product.find_elements(By.XPATH,value='./div'
        # #            # name_section=self.driver.find_element(By.XPATH,value='//section[@class="bop-section bop-intro"]')
            # name_tag=name_section.find_element(By.XPATH,value='//header[@class="bop-title"]')
            # names=name_tag.find_element(By.XPATH,value='//h1')
            # product_names.append(names) 
        #     tag_product_weight=self.driver.find_element(by=By.CLASS_NAME ,value="bop-title")
        #     weight=tag_product_weight.find_element(by=By.XPATH,value='.//span[@class="bop-catchWeight"]').text
        #     product_weight.append(weight)
        #     price=self.driver.find_element(by=By.XPATH,value='//h2[@class="bop-price__current " ]').text
        #     product_price.append(price)
        #     price_per=self.driver.find_element(by=By.XPATH,value='//span[@class="bop-price__per"]').text
        #     product_price_per.append(price_per)
        #     description=self.driver.find_element(by=By.XPATH,value='//div[@class="bop-info__content"]').text
        #     product_description.append(description)
        # dict={"unique_id":unique_id,
        #         "product_name":product_name,
        #         "product_weight":product_weight,
        #         "product_price":product_price,
        #         "product_price_per":product_price_per,
        #         "product_description":product_description}
        



            


        
        # food_products[0].click()
        # links=[]
        # for food_product in food_products:
        #     link=food_product.find_element(By.XPATH,value='//a').get_attribute('href')
        #     links.append(link)
        return food_products#
    
    


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
        





        

    









