from lxml import html
import requests
class NEW_PRODUCT:
    def __init__(self, name, full_price, current_price, currency):
        self.name = name
        self.full_price = full_price
        self.current_price = current_price
        self.currency = currency
        self.discount = "%0.2f" % (100 - (current_price / full_price * 100))
    def update(self, updated_price):
        self.current_price = updated_price
        self.discount = "%0.2f" % (100 - (updated_price / self.full_price * 100))
# Function to import product from Amazon
def price_extractor(str_price):
    from re import sub
    return float(sub("[^0-9,.]", "", (str_price.replace(',', '.'))))
def import_amazon_product(url):
    # user-agent for not resort to Amazon API
    headers = {'user-agent': 'Mozilla/5.0'}
    page = requests.get(url, headers=headers)   # page response
    tree = html.fromstring(page.content)        # html tree reading
    name = tree.xpath('//span[@id="productTitle"]/text()')[0].strip(' \n')
    str_price = tree.xpath('//span[@id="priceblock_ourprice"]/text()')
    current_price = price_extractor(str_price[0])
    try:
        full_price = price_extractor(tree.xpath('//span[@class="a-text-strike"]/text()')[0])
    except:
        full_price = current_price
    currency = str_price[0][0:3]
    new_amazon_product = NEW_PRODUCT(name, full_price, current_price, currency)
    return new_amazon_product.__dict__
