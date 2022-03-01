from bs4 import BeautifulSoup
import requests
import re
from datetime import datetime

url = "https://www.worldometers.info/coronavirus/country/india/"

page = requests.get(url)

page_html = BeautifulSoup( page.text , 'html.parser')

cases = page_html.find_all('span', text= re.compile('[0-9,].*'))

time = datetime.now()
print(f"Covid Stats in India as of {time.strftime('%d-%m-%Y %H:%M:%S')}\n")

print("Total Covid Cases Reported in India : ", cases[0].string)
print("Total Covid Death Reported in India : ", cases[1].string)
print("Total Covid Recovery  Reported in India : ", cases[2].string)


