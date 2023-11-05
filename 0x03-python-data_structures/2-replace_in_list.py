#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list

def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]

def print_list_integer(my_list=[]):
    for num in my_list:
        print(num)

# Test the functions
my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9

new_list = replace_in_list(my_list, idx, new_element)
print(new_list)
print(my_list)

print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

print_list_integer(my_list)
