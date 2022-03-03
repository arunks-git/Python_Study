from locators.quote_locator import QuoteLocator

class QuoteParser:
    def __init__(self,parent): ## here the argument is HTML codes for the parent of div and hence called parent. Hence can find childre inside it.
        self.parent = parent

    def __repr__(self):
        return f'<Quote {self.content} , by {self.author}>'

    @property
    def content(self):
        locator = QuoteLocator.CONTENT
        return self.parent.select_one(locator).string

    @property
    def author(self):
        locator = QuoteLocator.AUTHOR
        return self.parent.select_one(locator).string

    @property
    def tags(self):
        locator = QuoteLocator.TAGS
        return self.parent.select_one(locator).string
