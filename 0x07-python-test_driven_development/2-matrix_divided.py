#!/usr/bin/python3

def matrix_divided(matrix, div):
  """
  Divides all elements of a matrix.

  Args:
    matrix: A list of lists of integers or floats.
    div: A number (integer or float).

  Returns:
    A new matrix with all elements divided by div.

  Raises:
    TypeError: If matrix is not a matrix (list of lists) of integers/floats.
    TypeError: If each row of the matrix is not of the same size.
    TypeError: If div is not a number.
    ZeroDivisionError: If div is equal to 0.
  """

  if not isinstance(matrix, list):
    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

  for row in matrix:
    if not isinstance(row, list):
      raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if len(row) != len(matrix[0]):
      raise TypeError("Each row of the matrix must have the same size")

  if not isinstance(div, (int, float)):
    raise TypeError("div must be a number")

  if div == 0:
    raise ZeroDivisionError("division by zero")

  new_matrix = []
  for row in matrix:
    new_row = []
    for element in row:
      new_element = round(element / div, 2)
      new_row.append(new_element)
    new_matrix.append(new_row)

  return new_matrix


if __name__ == "__main__":
  matrix = [[1, 2, 3], [4, 5, 6]]
  div = 2
  new_matrix = matrix_divided(matrix, div)
  print(new_matrix)
