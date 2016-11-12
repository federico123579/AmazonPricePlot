import os
def add_to_data(key_to_add="", value_to_key=""):
    with open("data.txt", "rb+") as f:
        lines = f.readlines()
    os.remove("data.txt")
    with open("data.txt", "w") as f:
        for x, val in enumerate(lines):
            if key_to_add == value_to_key == "":
                f.write(val.strip('\n'))
            else:
                val = eval(val.strip('\n'))
                val[key_to_add] = value_to_key
                f.write(str(val) + '\n')

key_to_add = raw_input("KEY TO ADD: ")
value_to_key = raw_input("VALUE TO KEY: ")
add_to_data(key_to_add, value_to_key)
