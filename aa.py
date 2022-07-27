from multiprocessing.sharedctypes import Value
from selenium import webdriver
import uuid
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import shutil
import urllib.request
import json
import requests
import selenium
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




