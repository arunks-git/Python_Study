from bs4 import BeautifulSoup
import requests
import re

url = "https://groww.in/markets/top-gainers"

page = requests.get(url) # get the url

doc = BeautifulSoup(page.text,'html.parser')  # parse the page as HTML
body = doc.tbody # filtering out table body with tbody
trs = body.contents # filtering out content ( tags) in table

print("Top Stock Gainers \n")
print("Stock                                    CMP                  Change               Change % \n")
for tr in trs:  # traverse through each line in tbody
    name  =  tr.contents[0]   # filter out line 0 since that got the name
    price = tr.contents[2]     # filter out line 2 since that got the price
    stock_name = name.a.string   # Name is in 'a' tag and filter out
    price1 = price.find_all(text= re.compile('[0-9,].*'))  # filtering out prices using regex and putting in list
    print("%-40s %-20s %-20s %-20s "%(stock_name,price1[0],price1[1],price1[2]))


####### Another way by using CSS

for tr in body:
    locator1 = 'table.tb10Table tbody tr td a'  ## find the locator tree
    locator2 = 'table.tb10Table tbody tr td.fs14.fw500'
    locator3 = 'table.tb10Table tbody tr td.fs14.fw500 div.fs12.primaryClr'
    link1 = tr.select_one(locator1)  ## use select_one and filter the value
    link2 = tr.select_one(locator2)
    stock5 = link1.attrs['title']   ## use html hierarcy or regular expressions.
    print(stock5)
