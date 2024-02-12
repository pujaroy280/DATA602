#Q1 Fix all the syntax and logical errors in the given source code 
#add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the 
# average is a high score. The high score variable holds the value that is considered a high score.

HIGH_SCORE = 95
 
# Get the test scores.
test1 = float(input('Enter the score for test 1: ')) # Convert input to float
test2 = float(input('Enter the score for test 2: '))
test3 = float(input('Enter the score for test 3: ')) # Missing test3 input with conversion to float

# Calculate the average test score.
average = (test1 + test2 + test3) / 3 #Added parenthesis to ensure correct calculation.
# Print the average.
print('The average score is', average)
# If the average is a high score,
# congratulate the user.
if average >= HIGH_SCORE: # Correct the variable name from lowercase to uppercase as mentioned above in the variable.
    print('Congratulations!')
    print('That is a great average!') # Indented the print statement inside the if conditional statement.
else: # Added a else statement to verify what the outcome would be if the test scores were low.
    print('That is below average :(') # Conditional statement is complete.
#Q2
#The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width of two rectangles and prints to the user the area of both rectangles. 

# First, obtain the dimensions of the first rectangle
length1 = float(input('Enter the length of the first rectangle: '))
width1 = float(input('Enter the width of the first rectangle: '))

# Calculate the area of the first rectangle
area1 = length1 * width1

# Them, obtain the dimensions of the second rectangle
length2 = float(input('Enter the length of the second rectangle: '))
width2 = float(input('Enter the width of the second rectangle: '))

# Calculate the area of the second rectangle
area2 = length2 * width2

# Print the areas of both rectangles
print('Area of the first rectangle:', area1)
print('Area of the second rectangle:', area2)

#Q3 
#Ask a user to enter their first name and their age and assign it to the variables name and age. 
#The variable name should be a string and the variable age should be an int.  

#Using the variables name and age, print a message to the user stating something along the lines of:
# "Happy birthday, name!  You are age years old today!"

# Prompt the user to enter their first name
name = input('Enter your first name: ') # Value entered should be a string

# Prompt the user to enter their age
age = int(input('Enter your age: ')) # Conversion of the variable is an integer

# Print the birthday greeting
print(f'Happy birthday, {name}! You are {age} years old today!')

