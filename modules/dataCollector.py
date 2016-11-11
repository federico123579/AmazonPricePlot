def collect_data():
    products_matrix = []                    # initialization matrix
    with open("data/data.txt") as f:
        lines = f.readlines()               # read data already registered
    for x, val in enumerate(lines):         # for line in data
        products_matrix.append(eval(val))         # append line in matrix
    return products_matrix

def delete_last_line(link_to_file):
    with open(link_to_file, 'r') as f:
        lines = f.readlines()
    with open(link_to_file, 'w') as f:
        f.writelines([item for item in lines[:-1]])

def convert_first_line(name):
    import fileinput
    new_line = 'Date,' + name
    with open("data/price-data.txt") as f:
        line_test = f.readline()
    file_data = fileinput.input("data/price-data.txt", inplace=True)
    for line in file_data:
        if line_test == line:
            print new_line
        else:
            print line.strip('\n')

def write_data(products_matrix):
    import datetime
    now = datetime.datetime.now()
    with open("data/price-data.txt") as f:
        lines = f.readlines()
    if int(lines[-1][8:10]) == int(now.day):
        delete_last_line('data/price-data.txt')
    for x, val in enumerate(products_matrix):
        if x == 0:
            name = val['name']
            price = str(val['current_price'])
        else:
            name = name + ',' + val['name']
            price = price + ',' + str(val['current_price'])
    convert_first_line(name)
    with open("data/price-data.txt", "a") as f:
        f.write('%02d' % now.year + '-' + '%02d' % now.month + '-' + '%02d' % now.day + ',' + price)
