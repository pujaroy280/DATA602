"""
Puja Roy
2/18/24
QOTW#4
"""

"""
1. Write a function to calculate the area and perimeter of a rectangle.
"""
def rectangle_props(length, width):  # Define the function and add parameters as arguments to pass in
    area = length * width # Formula for area
    perimeter = 2 * (length + width) # Formula for perimeter
    return area, perimeter  # Return the values of the function into the variables area and perimeter

length = 7
width = 3
area, perimeter = rectangle_props(length, width)
print("Area:", area)
print("Perimeter:", perimeter)

"""
2. Write a function to check if a number is even or not.  The function should indicate to the user even or odd.
"""
def check_even_odd(num):
    if num % 2 == 0:  # If num is divisible by 2 then it will return even or else odd
        return "Even"
    else:
        return "Odd"

num = 10
print(num, "is", check_even_odd(num))

"""
3. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

Sample string: “CUNY sps”
# of upper case characters: 4
# of lower case characters: 3

"""

def count_case_characs(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

sample_string = "CUNY sps"
upper_count, lower_count = count_case_characs(sample_string)
print("# of upper case characters:", upper_count)
print("# of lower case characters:", lower_count)

"""
4. Write a Python function to sum all the numbers in a list
"""
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

numbers = [2, 4, 6, 8, 10]
print("Sum of the numbers in the list:", sum_list(numbers))

"""
5. Create a function that shows an example of global vs local variables.
"""
global_variable = 10

def function_with_local_variable():
    local_variable = 5
    print("Inside function:", local_variable) # accessing local variable
    print("Inside function:", global_variable) # accessing global variable

function_with_local_variable()
print("Outside function:", global_variable) # accessing global variable

"""
6. Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
"""
def multiply_with_unknown_number(arg):
    unknown_number = 23
    return arg * unknown_number

arg = 5
result = multiply_with_unknown_number(arg)
print("Result:", result)
