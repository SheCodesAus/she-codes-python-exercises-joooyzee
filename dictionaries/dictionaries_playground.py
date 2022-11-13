### LIST OF LISTS
groceries_list = [
["Baby Spinach", 2.78],
["Hot Chocolate", 3.70],
["Crackers", 2.10],
["Bacon", 9.00],
["Carrots", 0.56],
["Oranges", 3.08]
]

# get the price of bacon using a list of lists
price_of_bacon = groceries_list[3][1]
# print(price_of_bacon)

### DICTIONARIES
# dictionaries are mappings of key-value pairs
# syntax:
my_dict = {
    'key1': 'value1',
    'key2' : 'value2'
}

# our previous groceries list as a dictionary:
groceries_dict = {
    'Baby Spinach': 2.78,
    'Hot Chocolate': 3.70,
    'Crackers': 2.10,
    'Bacon': 9.00,
    'Carrots': 0.56,
    'Oranges': 3.08
}

# get price of bacon using a dictionary
print("====dictionary====")
price_of_bacon = groceries_dict['Bacon']
# print(price_of_bacon)

# add a new item
# NOTE: no need to use 'append', 'extend', etc.
groceries_dict['Avocadoes'] = 1.00
# print(groceries_dict)

# change existing item
groceries_dict['Hot Chocolate'] = 2.70
# print(groceries_dict)

# removing an item
del groceries_dict['Crackers']
# print(groceries_dict)

# iterating over a dictionary
print("-----method 1: iterating directly over the dictionary-----")
for item in groceries_dict:
    # print(item) # 'item' is our key i.e.g 'Baby Spinach'
    value_of_item = groceries_dict[item] # groceries_dict['Baby Spinach']
    print(f"{item}: ${value_of_item}")

print("-----method 2: iterating over dictionary keys or values using .keys() and .values()-----")
# can choose to explicitly iterate over all keys or values in a dictionary
for item in groceries_dict.keys():
    print(item)

for item in groceries_dict.values():
    print(item)

print("-----method 3: iterating over dictionary using .items()------")
for item in groceries_dict.items():
    print(item) # item is a tuple of the key-value pair, i.e. ('Baby Spinach', 2.78)
    # print(price)
    print(f"{item[0]}: ${item[1]}")

# tuple unpacking
for item, price in groceries_dict.items():
    # print(item)
    # print(price)
    print(f"{item}: ${price}")
