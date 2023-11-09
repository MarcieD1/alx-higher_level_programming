#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    result_dict = {}
    
    
    for key, value in a_dictionary.items():
        result_dict[key] = value * 2
    return result_dict


input_dict = {'a': 1, 'b': 2, 'c': 3}
new_dict = multiply_by_2(input_dict)
print(new_dict)
