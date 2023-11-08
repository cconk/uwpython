# ------------------------------------------------------------------------------------------ #
# Title: Assignment02
# Desc: This assignment demonstrates using constants, variables,
#         operators, formatting, and files and calculations
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Chad Conklin,10/17/2023, Modified Script
# ------------------------------------------------------------------------------------------ 

# Define the Data Constants
COURSE_NAME: str = "Python 100"
COURSE_PRICE: float = 999.98
STATE_TAX: float = 0.09
TOTAL_PRICE: float = COURSE_PRICE + COURSE_PRICE * STATE_TAX
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables
student_first_name: str = ""
student_last_name: str = ""
course_name: str = ""
csv_data: str = ""
file_obj: object = None

# Get data from the user and provide a looping mechanism to facilitate multiple entries
while True:
     # Input: Prompt for the student's first and last name
    student_first_name = input("Enter the student's first name: ")
    student_last_name = input("Enter the student's last name: ")

    # Present the data to the user in a formatted manner
    csv_data = f"{student_first_name},{student_last_name},{COURSE_NAME},{COURSE_PRICE},{TOTAL_PRICE}"
    print(csv_data)

    # Process the data to a file and provide error handling in case the file is not available for writing
    try:
        with open(FILE_NAME, mode="a") as file_obj:
            file_obj.write(csv_data + "\n")
    except IOError as e:
        print(f"Error writing to file: {e}")
        
     # Ask the user if they want to add more students as part of looping mechanism and exit option
    another_student = input("Do you want to add another student? (yes/no): ")
    if another_student.lower() != "yes":
        if file_obj:
            file_obj.close()
        break
