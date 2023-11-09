#!/usr/bin/python3

def unique_add(my_list=[]):
    unique_list = set(my_list)
    num = 0
    for i in unique_list:
        num += i
    return num

if __name__ == "__main__":
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = unique_add(my_list)
    print("Result: {:d}".format(result))
