from lxml import html
import requests
class NEW_PRODUCT:
    def __init__(self, name="", service="", full_price="", current_price="", currency=""):
        self.name = name
        self.full_price = full_price
        self.current_price = current_price
        self.currency = currency
        self.discount = "%0.2f" % (100 - (current_price / full_price * 100))
        self.service = service
# Function to import product from Amazon
def price_extractor(str_price):
    from re import sub
    return float(sub("[^0-9,.]", "", (str_price.replace(',', '.'))))
def import_product(url):
    if url.find("amazon") != -1:
        service = "amazon"
        xpath_set={'name': '//span[@id="productTitle"]/text()', 'current_price': '//span[@id="priceblock_ourprice"]/text()', 'full_price': '//span[@class="a-text-strike"]/text()'}
    else:
        print "ERROR: service not found"
        return -1
    # user-agent for not resort to Amazon API
    headers = {'user-agent': 'Mozilla/5.0'}
    page = requests.get(url, headers=headers)   # page response
    tree = html.fromstring(page.content)        # html tree reading
    name = tree.xpath(xpath_set['name'])[0].strip(' \n')
    str_price = tree.xpath(xpath_set['current_price'])[0].strip(" \t\n\r")
    current_price = price_extractor(str_price)
    try:
        full_price = price_extractor(tree.xpath(xpath_set['full_price'])[0])
    except:
        full_price = current_price
    if str_price.find("EUR") or str_price.find("\u20ac"):
        currency = "EUR"
    else:
        currency = ""
    new_product = NEW_PRODUCT(name, service, full_price, current_price, currency)
    return new_product.__dict__
