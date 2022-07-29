import requests
import selenium
from selenium.webdriver import Chrome

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
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

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver=Chrome(ChromeDriverManager().install())
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome() 
URL = "https://www.ocado.com/browse/fresh-chilled-food-20002/meat-poultry-42114"
driver.get(URL)
cookies_button=driver.find_element(by=By.XPATH,value='//*[@id="onetrust-accept-btn-handler"]')
cookies_button.click()
time.sleep(2)
product_link_list=[]
product_container=driver.find_element(by=By.XPATH,value='//*[@id="main-content"]/div[2]/div[2]/ul')
product_list=product_container.find_elements(by=By.XPATH,value='./li')
food=product_container.find_elements(by=By.XPATH,value='./li')[0]
food.click()
a=driver.find_element(by=By.CLASS_NAME,value='bop-price__per"]').text
#b=a.find_element(by=By.XPATH,value='./meta[@itemprop="priceCurrency"]').text
driver.close()
print(a)
