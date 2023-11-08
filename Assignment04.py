# ------------------------------------------------------------------------------------------ #
# Title: Assignment04
# Desc: This assignment demonstrates using lists and files to work with data
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Chad Conklin,11/01/2023, Updated Script for Assignment 4
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = """
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
"""
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables
student_first_name: str = ""  # Holds the first name of a student entered by the user.
student_last_name: str = ""  # Holds the last name of a student entered by the user.
course_name: str = ""  # Holds the name of a course entered by the user.
students: list = []  # A list of lists to hold student data.
new_students: list = []  # List of new students added via menu choice 1

# Load data from file into a list of lists on startup
with open(FILE_NAME, 'r') as file:
    for line in file:
        students.append(line.strip().split(','))

# Present and Process the data
while True:
    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":
        student_first_name = input("Enter the student's first name: ")
        student_last_name = input("Enter the student's last name: ")
        course_name = input("Please enter the name of the course: ")

        # Check if the student is already added to a particular course and if so skip adding them again
        if any(s[0] == student_first_name and s[1] == student_last_name and s[2] == course_name for s in students + new_students):
            print(f"{student_first_name} {student_last_name} is already registered for that course. Try another student or feel free to add {student_first_name} {student_last_name} to a course other than {course_name}.")
            continue
        
        new_students.append([student_first_name,student_last_name,course_name])
        continue
    
     # Present the current data
    elif menu_choice == "2":
        print("\nThe current data is:")
        for student in students:
            print(", ".join(student))
        print("\nNew students (not yet saved to file):")
        for student in new_students:
            print(", ".join(student))
        continue

    # Save the data to a file
    elif menu_choice == "3":
        with open(FILE_NAME, 'w') as file:
            combined_data = students + new_students
            for student in combined_data:
                file.write(",".join(student) + '\n')
        students.extend(new_students)
        new_students.clear()
        print(f"Data has been saved to {FILE_NAME}.")
        continue

    # Stop the loop
    elif menu_choice == "4":
        print("Program Ended")
        break  # out of the loop

    else:
        print("Please only choose option 1, 2, 3, or 4")
