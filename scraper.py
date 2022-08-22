from itertools import count, product
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
import os
import json
import urllib
import urllib.request
import boto3
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import inspect
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
        # filter_button=self.driver.find_element(By.XPATH,
        #                                 value='//*[@id="main-content"]/div[2]/div[3]/div[1]/div[3]/div[1]/form/span/select')
        # filter_button.click()
        # self.driver.implicitly_wait(1)
        # rating_button=self.driver.find_element(By.XPATH,
        #                         value='//*[@id="main-content"]/div[2]/div[3]/div[1]/div[3]/div[1]/form/span/select/option[9]')
        # rating_button.click()




    def find_links(self):
        self.accept_cookies()
        self.driver.implicitly_wait(1)
        self.browse_button()
        self.driver.implicitly_wait(1)
        self.search_bar()
        self.driver.implicitly_wait(1)
        time.sleep(1)
        links=[]
        self.driver.execute_script("window.scrollTo(0,1500)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(1500,3000)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(3000,3500)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(3500,4000)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(4000,4500)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(4500,6000)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(6000,7500)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(7500,9000)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(7500,9000)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(9000,10500)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(10500,12000)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(12000,13500)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(13500,15000)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(15000,16500)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(16500,18000)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(18000,19500)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(19500,21000)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(21000,22500)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(22500,25000)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(25000,26500)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(26500,28000)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(28000,29500)")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(29500,31000)")
        time.sleep(1)  
        link_containers=self.driver.find_elements(By.XPATH,
                                 value="//*[@id='main-content']/div[2]/div[3]/ul//li//div[@class='fop-contentWrapper']/a")

        for link_container in link_containers:
            link=link_container.get_attribute('href')
            links.append(link)
        return links





    def get_info(self):
        directory = "raw_data"
        parent_dir = "C:/Users/44772/Documents/GitHub/Data-Collection-Pipeline"
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)
        links=self.find_links()

        for link in links:
            # if link=='https://www.ocado.com/products/m-s-smokin-southern-fried-chicken-tenders-587598011'or link=='https://www.ocado.com/products/m-s-crackin-classic-chicken-tenders-587592011' or link=='https://www.ocado.com/products/gilberts-chicken-hot-dog-575079011':
            #     continue
            data_container={}
            uuid=uuid4().hex
            self.driver.get(link)
            name=self.driver.find_element(By.XPATH,
                        value='//header[@class="bop-title"]/h1').text


            price=self.driver.find_element(By.XPATH,
                            value='//*[@id="overview"]/section[2]/div[1]/div/h2').text



            rating_score=self.driver.find_element(By.XPATH,
                             value='//*[@id="reviews"]/div[1]/div[1]/span').text


            five_stars_rating=self.driver.find_element(By.XPATH,
                                value='//*[@id="reviews"]/div[1]/div[2]/div[1]/span').text

            four_stars_rating=self.driver.find_element(By.XPATH,
                                value='//*[@id="reviews"]/div[1]/div[2]/div[2]/span').text


            three_stars_rating=self.driver.find_element(By.XPATH,
                                value='//*[@id="reviews"]/div[1]/div[2]/div[3]/span').text

            two_stars_rating=self.driver.find_element(By.XPATH,
                            value='//*[@id="reviews"]/div[1]/div[2]/div[4]/span').text


            one_star_rating=self.driver.find_element(By.XPATH,
                            value='//*[@id="reviews"]/div[1]/div[2]/div[5]/span').text

            recommendation_rate=self.driver.find_element(By.XPATH,
                            value='//*[@id="reviews"]/div[1]/div[4]/div[1]').text
            img = self.driver.find_element(By.XPATH,value='//*[@id="overview"]/section[1]/div/div/div[1]/img')
            img_link=img.get_attribute('src')

        
            data_container = {
                    "price":price,
                    "product_name":name,
                    "rating_score":rating_score,
                    "recommendation_rate":recommendation_rate,
                    "five_stars_rating":five_stars_rating,
                    "four_stars_rating":four_stars_rating,
                    "three_stars_rating":three_stars_rating,
                    "two_stars_rating":two_stars_rating,
                    "one_star_rating":one_star_rating,
                    }
            data_table=pd.DataFrame(data_container,index=[0])
            engine=create_engine('postgresql+psycopg2://postgres:Feja0331@scraper.c0w7tms6lrlr.eu-west-2.rds.amazonaws.com:5432/scraper')
            inspect(engine).get_table_names()
            data_table.to_sql(f"{uuid}",engine,if_exists='append')
            file_name = f"{uuid}/data.json"
            os.makedirs(os.path.dirname(f"C:/Users/44772/Documents/GitHub/Data-Collection-Pipeline/raw_data/{file_name}"),exist_ok=True)
            with open(f"C:/Users/44772/Documents/GitHub/Data-Collection-Pipeline/raw_data/{file_name}", mode="w",encoding='utf-8') as file:
                file.write(str(data_container))
                file.close()
            os.mkdir(f"C:/Users/44772/Documents/GitHub/Data-Collection-Pipeline/raw_data/{uuid}/image/")
            urllib.request.urlretrieve(img_link, f"C:/Users/44772/Documents/GitHub/Data-Collection-Pipeline/raw_data/{uuid}/image/{uuid}.jpg")
            s3=boto3.client('s3')
            s3.upload_file(f'C:/Users/44772/Documents/GitHub/Data-Collection-Pipeline/raw_data/{file_name}','scraperaicore',f'{uuid}.json')
            s3.upload_file(f'C:/Users/44772/Documents/GitHub/Data-Collection-Pipeline/raw_data/{uuid}/image/{uuid}.jpg','scraperaicore',f'{uuid}.jpg')
    def upload_table(self):
        links=self.find_links()

        for link in links:
            # if link=='https://www.ocado.com/products/m-s-smokin-southern-fried-chicken-tenders-587598011'or link=='https://www.ocado.com/products/m-s-crackin-classic-chicken-tenders-587592011' or link=='https://www.ocado.com/products/gilberts-chicken-hot-dog-575079011':
            #     continue
            data_container={}
            uuid=uuid4().hex
            self.driver.get(link)
            name=self.driver.find_element(By.XPATH,
                        value='//header[@class="bop-title"]/h1').text


            price=self.driver.find_element(By.XPATH,
                            value='//*[@id="overview"]/section[2]/div[1]/div/h2').text



            rating_score=self.driver.find_element(By.XPATH,
                             value='//*[@id="reviews"]/div[1]/div[1]/span').text


            five_stars_rating=self.driver.find_element(By.XPATH,
                                value='//*[@id="reviews"]/div[1]/div[2]/div[1]/span').text

            four_stars_rating=self.driver.find_element(By.XPATH,
                                value='//*[@id="reviews"]/div[1]/div[2]/div[2]/span').text


            three_stars_rating=self.driver.find_element(By.XPATH,
                                value='//*[@id="reviews"]/div[1]/div[2]/div[3]/span').text

            two_stars_rating=self.driver.find_element(By.XPATH,
                            value='//*[@id="reviews"]/div[1]/div[2]/div[4]/span').text


            one_star_rating=self.driver.find_element(By.XPATH,
                            value='//*[@id="reviews"]/div[1]/div[2]/div[5]/span').text

            recommendation_rate=self.driver.find_element(By.XPATH,
                            value='//*[@id="reviews"]/div[1]/div[4]/div[1]').text        
            data_container = {
                    "price":price,
                    "product_name":name,
                    "rating_score":rating_score,
                    "recommendation_rate":recommendation_rate,
                    "five_stars_rating":five_stars_rating,
                    "four_stars_rating":four_stars_rating,
                    "three_stars_rating":three_stars_rating,
                    "two_stars_rating":two_stars_rating,
                    "one_star_rating":one_star_rating,
                    }
            data_table=pd.DataFrame(data_container,index=[0])
            engine=create_engine('postgresql+psycopg2://postgres:Feja0331@scraper.c0w7tms6lrlr.eu-west-2.rds.amazonaws.com:5432/scraper')
            inspect(engine).get_table_names()
            data_table.to_sql(f"{uuid}",engine,if_exists='append')









        

    









