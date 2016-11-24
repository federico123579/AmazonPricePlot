from lxml import html
import requests
import numpy as np
class NEW_PRODUCT:
    def __init__(self, name="", service="", full_price="", current_price="", currency=""):
        self.name = name
        self.full_price = full_price
        self.current_price = current_price
        self.currency = currency
        self.discount = "%0.2f" % (100 - (current_price / full_price * 100))
        self.service = service
class NEW_PRODUCT_ANALYSYS:
    def __init__(self ,entries={} ,url=''):
        self.service = found_service(url).lower()
        self.name = request_page(url).xpath(service_list[self.service]['xpath_set']['name'])[0].upper().strip(' ')
        self.url = url
        self.priceList = []
        for val in request_page(url).xpath(service_list[self.service]['xpath_set']['price_list']):
            val = float(val)
            self.priceList.append(val)
        self.average = np.mean(self.priceList)
        self.__dict__.update(entries)
    def update(self, **entries):
        self.__dict__.update(entries)
service_list = {
'amazon': {'xpath_set': {'name': '//span[@id="productTitle"]/text()', 'current_price': '//span[@id="priceblock_ourprice"]/text()', 'deal_price': '//span[@id="priceblock_dealprice"]/text()', 'full_price': '//span[@class="a-text-strike"]/text()'}},
'allkeyshop': {'xpath_set': {'name': '//span[@itemprop="name"]/text()', 'price_list': '//strong[@itemprop="price"]/@content'}}
}
# Function to import product from Amazon
def price_extractor(str_price):
    from re import sub
    return float(sub("[^0-9,.]", "", (str_price.replace(',', '.'))))
def found_service(url):
    if url.find("amazon") != -1:
        service = 'amazon'
    elif url.find("allkeyshop") != -1:
        service = 'allkeyshop'
    else:
        service = 'NotFound'
    return service
def request_page(url):
    # user-agent for not resort to Amazon API
    headers = {'user-agent': 'Mozilla/5.0'}
    page = requests.get(url, headers=headers)           # page response
    return html.fromstring(page.content)                # html tree reading
def import_product(url):
    service = found_service(url)
    xpath_set = service_list[service]['xpath_set']
    tree = request_page(url)                                   # request page content
    name = tree.xpath(xpath_set['name'])[0].strip(' \n')
    try:
        str_price = tree.xpath(xpath_set['current_price'])[0].strip(" \t\n\r")
    except:
        str_price = tree.xpath(xpath_set['deal_price'])[0].strip(" \t\n\r")
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
def import_price_analysys(url, old_analysys={}):
    tree = request_page(url)
    return NEW_PRODUCT_ANALYSYS(old_analysys, url)
