# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Chad Conklin,11/14/2023, Modified script to use functions and structured error handling
# ------------------------------------------------------------------------------------------ #
import json
import os
from typing import IO

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Data Variables
students: list = []  # a table of student data

#Classes
class FileProcessor:
    """Handles file processing tasks"""
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ Reads data from a file into student_data list """
        if not os.path.exists(file_name):
                # File does not exist, so we start with an empty list
                return
        try:
                with open(file_name, "r") as file:
                    # Ensure the file is not empty
                    file_content = file.read()
                    if file_content:
                        student_data.extend(json.loads(file_content))
                    else:
                        # File is empty, so we start with an empty list
                        return
        except json.JSONDecodeError as e:
                IO.output_error_messages("Error decoding JSON from file", e)     
        except Exception as e:
                IO.output_error_messages("Error reading file", e)
    
    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        try:
            with open(file_name, "w") as file:
                json.dump(student_data, file)
        except Exception as e:
            IO.output_error_messages("Error writing to file", e)

class IO:
    """ Handles Input/Output tasks """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        print(message)
        if error:
            print("-- Technical Error Message --")
            print(error)

    @staticmethod
    def output_menu(menu: str):
        print(menu)

    @staticmethod
    def input_menu_choice() -> str:
        return input("What would you like to do: ")

    @staticmethod
    def output_student_courses(student_data: list):
        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data() -> dict:
        try:
            first_name = input("Enter the student's first name: ")
            if not first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            last_name = input("Enter the student's last name: ")
            if not last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            return {"FirstName": first_name, "LastName": last_name, "CourseName": course_name}
        except ValueError as e:
            IO.output_error_messages(str(e))
            return {}

# Main processing
FileProcessor.read_data_from_file(FILE_NAME, students)

while True:
    IO.output_menu(MENU)
    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":
        student_info = IO.input_student_data()
        if student_info:
            students.append(student_info)
            print(f"You have registered {student_info['FirstName']} {student_info['LastName']} for {student_info['CourseName']}.")
    elif menu_choice == "2":
        IO.output_student_courses(students)
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(FILE_NAME, students)
        print("Data saved to file.")
    elif menu_choice == "4":
        break
    else:
        print("Please choose a valid option (1-4).")

print("Program Ended")
