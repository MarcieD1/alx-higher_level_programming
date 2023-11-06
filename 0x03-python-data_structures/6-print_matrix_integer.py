#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for row in matrix:
            for i in range(len(row)):
                if i != len(row) - 1:
                    print("{:d} ".format(row[i]), end="")
                else:
                    print("{:d}".format(row[i]))
                    

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print_matrix_integer(matrix)
    print("--")
    print_matrix_integer()
