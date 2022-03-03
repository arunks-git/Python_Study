from bs4 import BeautifulSoup

from locators.quote_page_locator import QuotesPageLocators
from parser.quote import QuoteParser

class QuotesPage:
    def __init__(self,page):
        self.soup = BeautifulSoup(page , 'html.parser')

    @property
    def quotes(self):
        locator = QuotesPageLocators.QUOTE
        quote_tag = self.soup.select(locator) ## Here we find div we looking for
        return [QuoteParser(e) for e in quote_tag]  ## pass each div to quote parser as argument . The quote parser will find parent to find children