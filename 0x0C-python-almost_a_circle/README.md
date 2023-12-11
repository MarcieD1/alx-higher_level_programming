# 0x0C-python-almost_a_circle

This project is about creating a Python package with a base class.

## 0. If it's not tested it doesn't work

All your files, classes and methods must be unit tested and be PEP 8 validated.

## 1. Base class

Writing the first class Base:

Create a folder named models with an empty file __init__.py inside - with this file, the folder will become a Python package

Create a file named models/base.py:

Class Base:

private class attribute __nb_objects = 0

class constructor: def __init__(self, id=None)::

if id is not None, assign the public instance attribute id with this argument value - you can assume id is an integer and you don’t need to test the type of it

otherwise, increment __nb_objects and assign the new value to the public instance attribute id

This class will be the “base” of all other classes in this project. The goal of it is to manage id attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)

## 2. Rectangle

mandatory
Write a class Rectangle that inherits from Base.

The class constructor should have the following parameters:

width: an integer representing the width of the rectangle

height: an integer representing the height of the rectangle

The class should have the following public methods:

def area(self): 
 
""" 
Returns the area of the circle. 
 
Args: 
    self: an instance of the Circle class 
 
Returns: 
    an integer representing the area of the circle 
"""
def perimeter(self):

"""
Returns the perimeter of the circle.

Args:
    self: an instance of the Circle class

Returns:
    an integer representing the perimeter of the circle
"""
## 5. Test cases 
 
mandatory 
Write unit tests for the Rectangle, Square, and Circle classes. 
 
## 6. Documentation 
 
mandatory 
Write documentation for the Rectangle, Square, and Circle classes. 
 
## 7. Submission 
 
Submit the following files to your GitHub repository: 
 
- README.md 
- models/base.py 
- models/rectangle.py 
- models/square.py 
- models/circle.py 
- tests/test_rectangle.py 
- tests/test_square.py 
- tests/test_circle.py
