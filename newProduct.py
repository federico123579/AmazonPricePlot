import sys                              # Import from the folder modules
sys.path.insert(0, 'modules')
import priceImporter

url = raw_input("URL: ")                # url to the new product
with open("data/list.txt", 'a') as f:   # appending the url on list.txt
    f.write(url + '\n')
product_dict = priceImporter.import_product(url)
with open("data/data.txt", "a") as f:   # appending data on data.txt
    f.write(str(product_dict) + '\n')
