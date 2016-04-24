import urllib2
import json
from Scrape import Scrape


def build_results(scrape):
    """Builds the json"""
    struct = {
        'results': [],
        'total': 0
    }
    titles = scrape.get_elems('.//*[@class="productInfo"]/h3/a/text()')
    links = scrape.get_elems('.//*[@class="productInfo"]/h3/a/@href')
    unit_prices = scrape.get_elems('.//*[@class="pricePerUnit"]/text()')

    sizes = []
    descriptions = []
    total = 0
    for link in links:
        s = Scrape(link)
        description = s.get_elems('.//*[@class="productText"]/p/text()')[0]
        descriptions.append(description)
        r = urllib2.urlopen(link)
        sizes.append(round(float(len(r.read())) / 1024, 2))

    for i in range(len(titles)):
        data = {
            "title": titles[i],
            "size": '{}kb'.format(str(sizes[i])),
            "unit_price": unit_prices[i][6:],
            "description": descriptions[i]
        }
        total += float(unit_prices[i][6:])
        struct['results'].append(data)

    struct['total'] = round(total, 2)
    return json.dumps(struct, indent=4, sort_keys=True)

if __name__ == "__main__":
    # Scraping page and printing output
    s = Scrape('http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/5_products.html')
    res = build_results(s)
    print res
