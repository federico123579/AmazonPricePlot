import sys                              # Import from the folder modules
sys.path.insert(0, 'modules')
import dataCollector, grapher
dataCollector.upadte_full_file_data("data/data.txt", "data/list.txt")
dataCollector.write_data(dataCollector.collect_data())
grapher.linear_graph("data/price-data.txt", "Amazon Prices", "amazon-price-date", dataCollector.collect_data())
