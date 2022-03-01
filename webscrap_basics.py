from bs4 import BeautifulSoup

with open('html_example.html', 'r') as f:
    doc = BeautifulSoup(f,'html.parser')

print(doc.prettify())

tag = doc.title.string

print(tag)

tags = doc.find('p')
tags1 = doc.find_all('p')
print(tags , tags1)