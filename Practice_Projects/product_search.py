from bs4 import BeautifulSoup
import requests
import re
from datetime import datetime

product = input("Enter the product code : ")
url =  f"https://www.newegg.com/global/in-en/p/pl?d={product}"

page = requests.get(url) # get the url
page_html = BeautifulSoup(page.text, 'html.parser')

items_table = page_html.find(class_='item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell')
items = items_table.find_all(text=re.compile(product))

final_items = {}

for item in items:
    parent = item.parent   ## Find the parent of each item in list to find link and price
    if parent.name == 'a':   ## The link is in 'a" string
        link = parent['href']  ## The link is href

    parent1 = item.find_parent(class_="item-container")  ## find the parent in html type
    price = parent1.find(class_="price-current").find_all(text=re.compile('[0-9,].*'))  ## further find the price

    final_items[item] = {"price" : int(price[0].replace(",","").replace("₹","")) , "link" : link } ## save as dictionary


### Sorting a dictionary can be done by converting into tuple and then using sort function
## Here the sorted function take two arguments. First is converting final_items dictonary into tuples by items() function.
## Then , the lambda functions takes tuple as argument and returns the price value in 1st index position

sorted_result = sorted(final_items.items() , key = lambda x: x[1]['price'])

for i in sorted_result:
    print(i[0])
    print("\nPrice is " , i[1]['price'])  # print the price which is a tuple and in 1st index
    print("\nLink is ", i[1]['link']) # print the link which is a tuple and in 1st index
    print("---------------------------")


