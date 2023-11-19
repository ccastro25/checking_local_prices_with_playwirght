
from insert_data_to_mysql import insert_data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from datetime import  datetime
import geocoder
   
today = datetime.now().date()
#ls or oz 
#eggs has to be searched as egg. some items have egg 
grocery_list =[
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
                'Platano',
                'Frozen+pizza'
                'Grapes',
                'Strawberry',
                'Blueberry', 
                'Raspberry',
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
def get_products(item):

lat_and_lon = geocoder.ip('me')
store_location = lat_and_lon.json['city']+' Store'
driver = webdriver.Safari()
# driver.get("https://www.walmart.com/search?q={0}".format(item))
driver.get("https://www.walmart.com/search?q=Bacon")
time.sleep(3)
soup = BeautifulSoup(driver.page_source)
# better way to targe titles and prices 
titles = soup.find_all(attrs={"data-automation-id":"product-title"})
prices =soup.find_all(attrs={"data-automation-id":"product-price"})
products = []
for i, v in enumerate(titles):
    price = prices[i].text.split('$')
    filtered_price = price[len(price)-1]
    products.append((titles[i].text,prices[i].text,today))
driver.quit()
print(products) 
return products




price = split('$')
filtered_price = price[len(price)-1]

final_list = []
for item in grocery_list:
    print("current item: {0}".format(item))
    final_list.extend( get_products(item))
    #may 120
    time.sleep(20)
    print("waiting 1 ") 
    time.sleep(20)
    print("waiting 2")
    time.sleep(20)
    print("waiting 3")
    time.sleep(20)
    '''print("waiting 4")
    time.sleep(20)
    print("waiting 5")
    time.sleep(20)'''
    print("done")

list_of_tupples =[]
for items in  products:
    list_of_tupples.append(tuple(items))

print(final_list)

#insert_data(list_of_tupples)
