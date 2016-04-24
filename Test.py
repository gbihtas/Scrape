from Scrape import Scrape
from main import build_results
import json
import unittest


class TestScrape(unittest.TestCase):

    def setUp(self):
        self.s = Scrape('http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/5_products.html')

    def test_get_elems_titles(self):
        """
        Test that the correct titles are returned
        """
        titles = self.s.get_elems('.//*[@class="productInfo"]/h3/a/text()')
        expected_outcome = [
            "Sainsbury's Apricot Ripe & Ready x5",
            "Sainsbury's Avocado Ripe & Ready XL Loose 300g",
            "Sainsbury's Avocado, Ripe & Ready x2",
            "Sainsbury's Avocados, Ripe & Ready x4",
            "Sainsbury's Conference Pears, Ripe & Ready x4 (minimum)",
            "Sainsbury's Golden Kiwi x4", "Sainsbury's Kiwi Fruit, Ripe & Ready x4"
        ]
        self.assertEqual(titles, expected_outcome)

    def test_get_elems_links(self):
        """
        Tests that the correct links are returned
        """
        links = self.s.get_elems('.//*[@class="productInfo"]/h3/a/@href')
        expected_outcome = [
            'http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/sainsburys-apricot-ripe---ready-320g.html',
            'http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/sainsburys-avocado-xl-pinkerton-loose-300g.html',
            'http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/sainsburys-avocado--ripe---ready-x2.html',
            'http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/sainsburys-avocados--ripe---ready-x4.html',
            'http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/sainsburys-conference-pears--ripe---ready-x4-%28minimum%29.html',
            'http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/sainsburys-golden-kiwi--taste-the-difference-x4-685641-p-44.html',
            'http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/sainsburys-kiwi-fruit--ripe---ready-x4.html'
        ]
        self.assertEqual(links, expected_outcome)

    def test_get_elems_unit_prices(self):
        """
        Tests that the correct unit prices are returned
        """
        unit_prices = self.s.get_elems('.//*[@class="pricePerUnit"]/text()')
        unit_prices = [price[6:] for price in unit_prices]
        expected_outcome = ['3.50', '1.50', '1.80', '3.20', '1.50', '1.80', '1.80']
        self.assertEqual(unit_prices, expected_outcome)

    def test_get_elems_description(self):
        """
        Tests that the correct description is returned
        """
        s = Scrape('http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/sainsburys-apricot-ripe---ready-320g.html')
        description = s.get_elems('.//*[@class="productText"]/p/text()')[0]
        expected_outcome = 'Apricots'
        self.assertEqual(description, expected_outcome)

    def test_build_results(self):
        """
        Tests that build_results returns correct data
        """
        res = json.loads(build_results(self.s))

        # tests 'total' is correct
        total = res['total'] == 15.1

        # tests results first entry is correct
        d = {
            "description": "Apricots",
            "size": "38.27kb",
            "title": "Sainsbury's Apricot Ripe & Ready x5",
            "unit_price": "3.50"
        }
        first_entry = res['results'][0] == d

        outcome = (total, first_entry)
        expected_outcome = (True, True)
        self.assertEqual(outcome, expected_outcome)

if __name__ == '__main__':
    unittest.main()
