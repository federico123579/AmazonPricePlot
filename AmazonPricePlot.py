import sys                              # Import from the folder modules
sys.path.insert(0, 'modules')
import dataCollector

dataCollector.write_data(dataCollector.collect_data())
