"""
Puja Roy
Assignment#3
2/18/24
"""

"""
Q1: Write a program that prompts the user for a meal: breakfast, lunch, or dinner. Then using if statements and else statements print the user a message recommending a meal. For example, if the meal was breakfast, you could say something like, “How about some bacon and eggs?”
The user may enter something else in, but you only have to respond to breakfast, lunch, or dinner.
"""
meal = input("What meal are you planning to devour? (breakfast, lunch, or dinner): ")

# .lower method is to handle scenarios where the user types in values that are in CAPS
if meal.lower() == "breakfast":
    print("How about some bacon and eggs?")
elif meal.lower() == "lunch":
    print("How about a tuna sandwich or chicken salad?")
elif meal.lower() == "dinner":
    print("How about some mutton soup, rice, shrimp and vegetables?")
else:
    print("Apologies, I can only recommend meals for breakfast, lunch, or dinner.")

"""
Q2: The mailroom has asked you to design a simple payroll program that calculates a student employee’s gross pay, including any overtime wages. If any employee works over 20 hours in a week, the mailroom pays them 1.5 times their regular hourly pay rate for all hours over 20. 
You should take in the user’s input for the number of hours worked, and their rate of pay.
"""

# Obtain user input for number of hours worked and hourly pay rate
hours_worked = float(input("Enter the number of hours worked this week: "))
hourly_pay_rate = float(input("Enter the hourly pay rate: "))

# Calculate gross pay without overtime
if hours_worked <= 20:
    gross_pay = hours_worked * hourly_pay_rate
else:
    # Calculate gross pay with overtime
    regular_hours = 20
    overtime_hours = hours_worked - regular_hours
    regular_pay = regular_hours * hourly_pay_rate
    overtime_pay = overtime_hours * (hourly_pay_rate * 1.5)
    gross_pay = regular_pay + overtime_pay

# Display the gross pay by printing the message
print("Gross pay for the week: $", format(gross_pay, ".2f")) #gross pay is displayed with a precision of two decimal places using the format() function.

"""
Q3: Write a function named times_ten. The function should accept an argument and display the product of its argument multiplied times 10.
"""

def times_ten(number):
    result = number * 10
    print("The product of", number, "multiplied by 10 is:", result)

# Example usage of the function
times_ten(5)
times_ten(28)
times_ten(100)

"""
Q4: Find the errors, debug the program, and then execute to show the output.

def main()
      Calories1 = input( "How many calories are in the first food?")
      Calories2 = input( "How many calories are in the first food?")
      showCalories(calories1, calories2)

def showCalories()   
   print(“The total calories you ate today”, format(calories1 + calories2,.2f))

"""
"""
Errors Discovered:
1. The variables declared at the beginning are not in correct syntax since the first letter is capitalized.
2. The input of the values are not parsed in as float.
3. The parameters including calories1 and calories2 in the second funtion showCalories are missing.
4. Calculation of total calories is missing in the second function.
5. The print statement in the second function is missing a semicolon in the string.
6. The print statement in the second function is supposed to have a variable named total_calories to print the total calories calculation.
"""
# Corrected version of the original program:
def main():
    calories1 = float(input("How many calories are in the first food?"))
    calories2 = float(input("How many calories are in the second food?"))
    showCalories(calories1, calories2)

def showCalories(calories1, calories2):  
    total_calories = calories1 + calories2
    print("The total calories you ate today:", format(total_calories, ".2f"))

# Call the main function to execute the program
main()

"""
Q5: Write a program that uses any loop (while or for) that calculates the total of the following series of numbers:
         1/30 + 2/29 + 3/28 ............. + 30/1
"""

total = 0

# Iterate through the numbers from 1 to 30
for i in range(1, 31):
    # Calculate each term of the series and add it to the total
    term = i / (31 - i)
    total += term

print("The total of the series is:", total)

"""
Q6: Write a function that computes the area of a triangle given its base and height.
The formula for an area of a triangle is:
AREA = 1/2 * BASE * HEIGHT

For example, if the base was 5 and the height was 4, the area would be 10.
triangle_area(5, 4)   # should print 10
"""

#Define function called triangle_area that takes in 2 parameters base and the height as inputs
def triangle_area(base, height):
    area = 0.5 * base * height
    return area

# Example usage of the function
print(triangle_area(5, 4))  # Output: 10.0

print(triangle_area(7, 6))  # Output: 21.0
