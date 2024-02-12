# Puja Roy
# Assignment#2
# 2/10/24

# Q1. What will the following code display?
numbers = [1, 2, 3, 4, 5]
print(numbers[1:-5])

"""
The code above will display an empty list in brackets without any values.
"""
#Can you debug and fix the output? The code should return the entire list
numbers = [1, 2, 3, 4, 5]
print(numbers[0:5])
print(numbers[:])

# I used the slicing method to print the values starting from the index 0 and ending at index 5 to print all of the values in the list.
# There is also another technique to print all the ways in the list by using the semicolon in brackets to slice the list from beginning to the end.

"""
Q2. Design a program that asks the user to enter a store’s sales for each day of the
week. The amounts should be stored in a list. Use a loop to calculate the total sales for
the week and display the result.
"""
# Define a function
def main():
    # Initialize an empty list to store sales for each day of the week
    sales = []

    # Loop through each day of the week and ask the user to input sales
    for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
        sales_input = float(input(f"Enter sales for {day}: $")) #Input of the user will be parsed as a float input.
        sales.append(sales_input) # adds the sales amount for a particular day of the week to the sales list.

    # Calculate the total sales for the week using the sum method
    total_sales = sum(sales)

    # Display the total sales for the week
    print(f"Total sales for the week: ${total_sales:.2f}")

if __name__ == "__main__":
    main()

"""
Q3. Create a list with at least 5 places you’d like to travel to. Make sure the list isn’t in
alphabetical order
● Print your list in its original order.
● Use the sort() function to arrange your list in order and reprint your list.
● Use the sort(reverse=True) and reprint your list.
"""

# Create a list of places to travel
places_to_travel = ["Switzerland", "India", "China", "Japan", "Korea"]

# Print the list in its original order
print("Original order:")
print(places_to_travel)

# sort() function to arrange the list in alphabetical order
places_to_travel.sort()
print("\nSorted order:")
print(places_to_travel)

# sort(reverse=True) function to arrange the list in reverse alphabetical order
places_to_travel.sort(reverse=True)
print("\nReverse sorted order:")
print(places_to_travel)

"""
Q4. Write a program that creates a dictionary containing course numbers and the room
numbers of the rooms where the courses meet. The program should also create a
dictionary containing course numbers and the names of the instructors that teach each
course. After that, the program should let the user enter a course number, then it should
display the course’s room number, instructor, and meeting time.
"""
#Define a function that contains dictionaries and a for loop to interate through the lists to print info containing course numbers, room numbers and meeting times.
def main():
    # Dictionary containing course numbers and room numbers
    room_numbers = {
        "DATA602": "Room 111",
        "DATA606": "Room 323",
        "DATA607": "Room 888",
        "DATA608": "Room 999"
    }

    # Dictionary containing course numbers and instructors
    instructors = {
        "DATA602": "Prof. Anderson",
        "DATA606": "Ms. Roy",
        "DATA607": "Dr. Brown",
        "DATA608": "Prof. Lucy"
    }

    # Dictionary containing course numbers and meeting times
    meeting_times = {
        "DATA602": "7:30 PM",
        "DATA606": "10:10 AM",
        "DATA607": "8:30 AM",
        "DATA608": "3:33 PM"
    }

    # Prompt the user to enter a course number
    course_number = input("Enter a course number (e.g., DATA602): ")

    # Display the course's room number, instructor, and meeting time
    if course_number in room_numbers:
        print(f"Room Number: {room_numbers[course_number]}")
        print(f"Instructor: {instructors[course_number]}")
        print(f"Meeting Time: {meeting_times[course_number]}")
    else:
        print("Course number not found.")

if __name__ == "__main__":
    main()

"""
Q5. Write a program that keeps names and email addresses in a dictionary as
key-value pairs. The program should then demonstrate the four options:
● look up a person’s email address,
● add a new name and email address,
● change an existing email address, and
● delete an existing name and email address.
"""
# Define a function to store names and email addresses in a dictionary and if else conditional statements to print certain options.
def main():
    # Dictionary to store names and email addresses
    contacts = {
        "Lucy Little": "lucy.little@gmail.com",
        "Anne Roy": "anne.roy@gmail.com",
        "Nancy Riverwood": "nancy.riverwood@gmail.com"
    }
    # Print the options the user will be prompted in the program.
    while True:
        print("\nOptions:")
        print("1. Search up a person's email address")
        print("2. Add a new name and email address")
        print("3. Change an existing email address")
        print("4. Delete an existing name and email address")
        print("5. Exit/Adjourn")

        choice = input("Enter your choice (1-5): ")  #Prompt the user

        if choice == "1":
            name = input("Enter the name to look up: ")
            if name in contacts:
                print(f"Email address: {contacts[name]}")
            else:
                print("Name not found.")

        elif choice == "2":
            name = input("Enter the new name: ")
            email = input("Enter the email address: ")
            contacts[name] = email
            print("Contact added.")

        elif choice == "3":
            name = input("Enter the name to change email address: ")
            if name in contacts:
                new_email = input("Enter the new email address: ")
                contacts[name] = new_email
                print("Email address updated.")
            else:
                print("Name not found.")

        elif choice == "4":
            name = input("Enter the name to delete: ")
            if name in contacts:
                del contacts[name]
                print("Contact deleted.")
            else:
                print("Name not found.")

        elif choice == "5":
            print("Exiting/adjourning the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()


