from lxml import html
import requests


class Scrape(object):
    """
    Scrapes a page and returns all elements as specified by xpath
    """
    def __init__(self, url):
        self.url = url
        self.page = requests.get(url)
        self.tree = html.fromstring(self.page.content)

    def get_elems(self, xpath):
        """
        This method gets and returns the data of all elements
        which have the given xpath
        """
        elems = []
        data = self.tree.xpath(xpath)
        for elem in data:
            if len(elem.strip()) > 0:
                elems.append(elem.strip())
        return elems
