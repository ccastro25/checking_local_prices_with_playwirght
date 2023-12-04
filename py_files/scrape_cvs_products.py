from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import  datetime
from bs4 import BeautifulSoup
import time
import re 
#class="css-901oao css-cens5h r-b0vftf r-1xaesmv r-ubezar r-majxgm r-29m4ib r-rjixqe r-1mnahxq r-fdjqy7 r-13qz1uu"
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
driver = webdriver.Chrome(options=options)

grocery_list =[ 'Raspberry',
                'Egg',
                'Milk',
                'Bread',
                'Bacon',
                'Cooking+oil',
                'Rice',
                'Tuna',
                'Steak',
                'Chicken', 
                'Ham', 
                'Cheese',
                'Yogurt', 
                'Banana',
                'Frozen+pizza',
                'Grapes',
                'Strawberry',
                'Blueberry', 
               
                'Lettuce', 
                'Tomatoes',
                'Onion',
                'Avocado',
                'Cereals',
                'Ice+cream',
                'Cream+cheese', 
                'Tomato+sauce',
                'Spaghetti', 
                'Lasagna+noodles', 
                'Chocolate', 
              ]
today = datetime.now().date()

def get_cvs_products(item):
    driver.get(f"https://www.cvs.com/search?searchTerm=milk")
    time.sleep(2)

    soup = BeautifulSoup(driver.page_source,'html.parser')
    price =soup.find_all('div',class_="css-901oao r-1xaesmv r-ubezar r-majxgm r-wk8lta")
    title =soup.find_all('div',class_="css-901oao css-cens5h r-b0vftf r-1xaesmv r-ubezar r-majxgm r-29m4ib r-rjixqe r-1mnahxq r-fdjqy7 r-13qz1uu")

    products =[]
    for i,v  in enumerate(title):
        products.append((title[i].text, re.sub('[^0-9,.]','',price[i].text), today, "CVS"))
        

    print('this is a sample')
    print(products)
    return products


products = []
for item in grocery_list:
    print(f"current item: {item}")
    products.extend( get_cvs_products(item))
    print("starting")
    time.sleep(20)
    print("waiting 1 ") 
    time.sleep(20)
    print("waiting 2")
    time.sleep(20)
    print("waiting 3")
    time.sleep(20)
    print("done")
driver.quit()

with open('acme.pickle','wb') as f:
    pickle.dump(final_list,f) 
insert_data(final_list,store_product)
