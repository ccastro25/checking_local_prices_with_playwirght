from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from grocery_list import grocery_list
from datetime import  datetime
from bs4 import BeautifulSoup
import time
import re
import pickle  
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton

options = webdriver.SafariOptions()
options.add_argument('--headless')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
driver = webdriver.Safari(options=options)
today = datetime.now().date()

def get_product(item):
    
    driver.get(f"https://www.cvs.com/search?searchTerm={item}")
    time.sleep(2)
    
  
    soup = BeautifulSoup(driver.page_source,'html.parser')
    price =soup.find_all('div',class_="css-901oao r-1xaesmv r-ubezar r-majxgm r-wk8lta")
    title =soup.find_all('div',class_="css-901oao css-cens5h r-b0vftf r-1xaesmv r-ubezar r-majxgm r-29m4ib r-rjixqe r-1mnahxq r-fdjqy7 r-13qz1uu")

    products =[]
    for i,v  in enumerate(title):
        products.append((title[i].text, re.sub('[^0-9,.]','',price[i].text), today, "CVS"))
      
    return products

def get_cvs_products():
    products = []
    clickable = driver.find_element(By.ID, "clickable")
    ActionChains(driver)\
        .click_and_hold(clickable)\
        .perform()
    text_input = driver.find_element(By.ID, "textInput")
    ActionChains(driver)\
        .send_keys_to_element(text_input, "abc")\
        .perform()

        
    for item in grocery_list:
        print(f"current item: {item}")
        products.extend( get_product(item))
        time.sleep(80) 
    driver.quit()
    return products    



