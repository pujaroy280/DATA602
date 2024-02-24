"""
Puja Roy
DATA 602
2/24/24
"""

"""
Q1: Create a class called BankAccount that has four attributes: bankname, firstname,
lastname, and balance.
The default balance should be set to 0.
In addition, create ...
● A method called deposit() that allows the user to make deposits into their balance.
● A method called withdrawal() that allows the user to withdraw from their balance.
● Withdrawal may not exceed the available balance. Hint: consider a conditional argument
in your withdrawal() method.
● Use the __str__() method in order to display the bank name, owner name, and current
balance.
● Make a series of deposits and withdrawals to test your class.
"""

# Create class named BankAccount
class BankAccount:  # Identify the aruguments and the objects
    def __init__(self, bankname, firstname, lastname, balance=0):
        self.bankname = bankname
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount

    def __str__(self):
        return f"Bank: {self.bankname}\nOwner: {self.firstname} {self.lastname}\nBalance: {self.balance}"


# Testing the BankAccount class
account = BankAccount("Lakshmi-Vishnu Bank", "Nancy", "Drew")
print(account)
account.deposit(2600)
account.withdrawal(300)
print(account)

"""
Q2: Create a class Box that has attributes length and width that takes values for length
and width upon construction (instantiation via the constructor).
In addition, create…
● A method called render() that prints out to the screen a box made with asterisks of
length and width dimensions
● A method called invert() that switches length and width with each other
● Methods get_area() and get_perimeter() that return appropriate geometric calculations
● A method called double() that doubles the size of the box. Hint: Pay attention to return
value here.
● Implement __eq__ so that two boxes can be compared using ==. Two boxes are equal if
their respective lengths and widths are identical.
● A method print_dim() that prints to screen the length and width details of the box
● A method get_dim() that returns a tuple containing the length and width of the box
● A method combine() that takes another box as an argument and increases the length
and width by the dimensions of the box passed in
● A method get_hypot() that finds the length of the diagonal that cuts through the middle
● Instantiate 3 boxes of dimensions 5,10 , 3,4 and 5,10 and assign to variables box1,
box2 and box3 respectively
● Print dimension info for each using print_dim()
● Evaluate if box1 == box2, and also evaluate if box1 == box3, print True or False to the
screen accordingly
● Combine box3 into box1 (i.e. box1.combine())
● Double the size of box2
● Combine box2 into box1
"""

import math

class Box:
    def __init__(self, length, width):
        # Initialize Box object with length and width attributes
        self.length = length
        self.width = width

    def render(self):
        # Print a box made of asterisks with dimensions length x width
        for _ in range(self.width):
            print('*' * self.length)

    def invert(self):
        # Swap length and width attributes
        self.length, self.width = self.width, self.length

    def get_area(self):
        # Calculate and return the area of the box
        return self.length * self.width

    def get_perimeter(self):
        # Calculate and return the perimeter of the box
        return 2 * (self.length + self.width)

    def double(self):
        # Double the dimensions of the box and return a new Box object with the updated dimensions
        return Box(self.length * 2, self.width * 2)

    def __eq__(self, other):
        # Check if two boxes are equal by comparing their lengths and widths
        return self.length == other.length and self.width == other.width

    def print_dim(self):
        # Print the dimensions of the box
        print(f"Length: {self.length}, Width: {self.width}")

    def get_dim(self):
        # Return a tuple containing the length and width of the box
        return self.length, self.width

    def combine(self, other):
        # Increase the dimensions of the box by adding the dimensions of another box
        self.length += other.length
        self.width += other.width

    def get_hypot(self):
        # Calculate and return the length of the diagonal that cuts through the middle of the box
        return math.sqrt(self.length**2 + self.width**2)


# Instantiate 3 boxes
box1 = Box(7, 20)
box2 = Box(5, 9)
box3 = Box(3, 16)

# Print dimension info for each
box1.print_dim()
box2.print_dim()
box3.print_dim()

# Evaluate if box1 == box2, and also evaluate if box1 == box3
print("Are box1 and box2 equal?", box1 == box2)
print("Are box1 and box3 equal?", box1 == box3)

# Combine box3 into box1
box1.combine(box3)
print("Combined box1:")
box1.print_dim()

# Double the size of box2
box2 = box2.double()
print("Doubled box2:")
box2.print_dim()

# Combine box2 into box1
box1.combine(box2)
print("Combined box1 with doubled box2:")
box1.print_dim()

