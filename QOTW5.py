"""
Puja Roy
DATA 602
2/24/24
"""

"""
1. Write a Python class to reverse a string word by word.

Example:
Input string : 'hello .py'
Expected Output : '.py hello'

"""
class ReverseString:
    def reverse_words(self, s):
        # Split the input string into words using whitespace as a separator
        words = s.split()
        # Reverse the list of words
        reversed_words = words[::-1]
        # Join the reversed words into a string with whitespace as separator
        reversed_string = ' '.join(reversed_words)
        return reversed_string

# Test the class
reverse_str = ReverseString()
input_string = 'hello .py'
output_string = reverse_str.reverse_words(input_string)
print("Input string:", input_string)
print("Expected Output:", output_string)

"""
2. Write a Python class named Circle constructed by a radius and two methods
which will compute the area and the perimeter of a circle.
"""

import math

class Circle:
    def __init__(self, radius):
        # Initialize Circle object with radius attribute
        self.radius = radius

    def area(self):
        # Calculate and return the area of the circle using the formula πr^2
        return math.pi * self.radius ** 2

    def perimeter(self):
        # Calculate and return the perimeter of the circle using the formula 2πr
        return 2 * math.pi * self.radius

# Test the class
circle = Circle(6)
print("Area of the circle:", circle.area())
print("Perimeter of the circle:", circle.perimeter())
