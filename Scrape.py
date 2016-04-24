from lxml import html
import requests


class Scrape(object):
    """Scrapes a page getting the following info:
        1. title of product
        2. link of product
        3. unit price of product
        4. size of the linked HTML

        Moreover, it follows the product's link to get its description.
    """
    def __init__(self, url):
        self.url = url
        self.page = requests.get(url)
        self.tree = html.fromstring(self.page.content)

    def get_elems(self, xpath):
        """
        This method get the data based of all element which have the
        given xpath
        """
        elems = []
        data = self.tree.xpath(xpath)
        for elem in data:
            if len(elem.strip()) > 0:
                elems.append(elem.strip())
        return elems
