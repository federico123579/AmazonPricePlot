import sys                              # Import from the folder modules
sys.path.insert(0, 'modules')
import dataCollector, grapher
import priceImporter
dataCollector.update_data("data/data.txt", "data/list.txt")
dataCollector.write_data(dataCollector.collect_data("data/data.txt"), "data/price-data.txt")
grapher.linear_graph("data/price-data.txt", "Amazon Prices", "amazon-price-date", dataCollector.collect_data("data/data.txt"))
dataCollector.write_average_data(priceImporter.import_price_analysys('http://www.allkeyshop.com/blog/buy-battlefield-1-cd-key-compare-prices/'), "data/average-data.txt")
#grapher.polynomial_graph()
