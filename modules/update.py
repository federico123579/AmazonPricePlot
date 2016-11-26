def add_to_data(data_file, key_to_add="", value_to_key=""):
    import fileinput
    file_data = fileinput.input(data_file, inplace=True)
    for line in file_data:
        if key_to_add == value_to_key == "":
            print line.strip('\n')
        else:
            val = eval(line)
            val[key_to_add] = value_to_key
            print val.strip('\n')
'''def delete_product(data_file, product_name):
    import fileinput
    file_data = fileinput.input(data_file, inplace=True)
    for line in file_data:
        if line.find(product_name) != -1:
            print line.replace(',' + product_name, '')
        else:
            print line'''
if __name__ == '__main__':
    key_to_add = raw_input("KEY TO ADD: ")
    value_to_key = raw_input("VALUE TO KEY: ")
    add_to_data("../data/data.txt", key_to_add, value_to_key)
