# ------------------------------------------------------------------------------------------ #
# Title: Assignment03
# Desc: This assignment demonstrates using conditional logic and looping
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Chad Conklin,10/24/2023, Modified Script for assignment 3
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants1


MENU = """
---- Course Registration Program ----
Select from the following menu:
1. Register a Student for a Course
2. Show current data
3. Save data to a file
4. Exit the program
-----------------------------------------
"""
FILE_NAME = "Enrollments.csv"

# Define the Data Variables
student_first_name = ""
student_last_name = ""
course_name = ""
csv_data = ""
file_obj = None
menu_choice = ""

# Present and Process the data1
while menu_choice != "4":
    # Present the menu of choices
    print(MENU)
    menu_choice = input("Enter your choice (1/2/3/4): ")

    if menu_choice == "1":
        # Input user data
        student_first_name = input("Enter the student's first name: ")
        student_last_name = input("Enter the student's last name: ")
        course_name = input("Enter the course name: ")
        # Present the current data
        csv_data = f"{student_first_name}, {student_last_name}, {course_name}"
        print(csv_data)
        print("Student registered successfully!\n")

    elif menu_choice == "2":
        if csv_data:
            print("Current data:")
            print(csv_data)
        else:
            print("No data to display.\n")

    # Save the data to a file
    elif menu_choice == "3":
        with open(FILE_NAME, 'a') as file:
            file.write(f"{student_first_name}, {student_last_name}, {course_name}\n")
        print(f"Data saved to {FILE_NAME}.\n")
          # Reset the local variable
        csv_data = ""

    # Stop the loop and exit the program
    elif menu_choice == "4":
        print("Exiting the program. Goodbye!")

    else:
        print("Invalid choice. Please select a valid option (1/2/3/4).\n")