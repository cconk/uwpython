# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot, 1/1/2030, Created Script
#   Chad Conklin, 11/13/2023, Enhanced with dictionaries, exception handling, and duplicate check
# ------------------------------------------------------------------------------------------ #
import json
# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables
students: list = []  # List of dictionaries for all students
menu_choice: str = ''  # Hold the choice made by the user

# Read file data into a list of dictionaries
try:
    with open(FILE_NAME, "r") as file:
        for row in file:
            first_name, last_name, course = row.strip().split(',')
            students.append({'First Name': first_name, 'Last Name': last_name, 'Course': course})
except FileNotFoundError:
    print(f"Warning: {FILE_NAME} not found, starting with empty data.")

# Function to check if student is already enrolled in a course
def is_student_enrolled(first_name, last_name, course):
    for student in students:
        if student['First Name'] == first_name and student['Last Name'] == last_name and student['Course'] == course:
            return True
    return False

# Present and Process the data
while True:
    print(MENU)
    menu_choice = input("What would you like to do: ")

    if menu_choice == "1":
        first_name = input("Enter the student's first name: ")
        last_name = input("Enter the student's last name: ")
        course = input("Please enter the name of the course: ")

        if is_student_enrolled(first_name, last_name, course):
            print(f"Student {first_name} {last_name} is already enrolled in {course}. Please try again.")
        else:
            students.append({'First Name': first_name, 'Last Name': last_name, 'Course': course})
            print(f"You have registered {first_name} {last_name} for {course}.")

    elif menu_choice == "2":
        print("-" * 50)
        for student in students:
            print(f"Student {student['First Name']} {student['Last Name']} is enrolled in {student['Course']}")
        print("-" * 50)

    elif menu_choice == "3":
        try:
            with open(FILE_NAME, "w") as file:
                for student in students:
                    csv_data = f"{student['First Name']},{student['Last Name']},{student['Course']}\n"
                    file.write(csv_data)
            with open("Enrollments.json", "w") as file:
                json.dump(students, file)
            print("The following data was saved to files!")
            for student in students:
                print(f"Student {student['First Name']} {student['Last Name']} is enrolled in {student['Course']}")
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")

    elif menu_choice == "4":
        break
    else:
        print("Please choose a valid option (1, 2, 3, or 4)")

print("Program Ended")