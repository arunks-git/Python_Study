import requests

from pages.quote_pages import QuotesPage

page_content = requests.get('https://quotes.toscrape.com/').content
page = QuotesPage(page_content)

for quote in page.quotes:
    print(quote)

'''
Description of project : 

1. App.py does the get calls and get the HTML content.
2. Then the QuotesPage is called to parse 
3. QuotesPage does the HTML parsing using BeautifulSoup package and return HTML code.
4. Using a for loop , each quote HTML is send to quotes function in QuotesPage
5. The quotes function locate the quote locator ( using QuotesPageLocators) and then extracts the div HTML code ( where quote parent are there)
6. Then it pass each div to quote parser as argument.
7. The repr function returns the quote and author name from the quoteparser class. 
It uses the quotelocator class to find the location the child - author , content and tags.

'''