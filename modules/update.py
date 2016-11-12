def add_to_data(data_file, key_to_add="", value_to_key=""):
    import os
    with open(data_file, "rb+") as f:
        lines = f.readlines()
    os.remove(data_file)
    with open(data_file, "w") as f:
        for x, val in enumerate(lines):
            if key_to_add == value_to_key == "":
                f.write(val.strip('\n'))
            else:
                val = eval(val.strip('\n'))
                val[key_to_add] = value_to_key
                f.write(str(val) + '\n')
if __name__ == '__main__':
    key_to_add = raw_input("KEY TO ADD: ")
    value_to_key = raw_input("VALUE TO KEY: ")
    add_to_data("../data/data.txt", key_to_add, value_to_key)
