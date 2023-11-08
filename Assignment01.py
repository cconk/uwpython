# ------------------------------------------------------------------------------------------ #
# Title: Assignment01
# Desc: This assignment demonstrates using constants, variables, and print()
# Change Log: (Who, When, What)
# Chad Conklin,10/01/2023, Created Script
# ------------------------------------------------------------------------------------------ 

COURSE_NAME = "Python 100"

student_first_name = input("What is your first name? ")
student_last_name = input("What is your last name? ")

# single line statement
print("Hello " + student_first_name + " " + student_last_name + " you are registered for " + COURSE_NAME + "!")

# multi-line statement
print("Hello " \
      + student_first_name + \
      " " + student_last_name + \
      " you are registered for " + \
        COURSE_NAME + "!")

# multi-line statement with new line
print("Hello " + "\n" + student_first_name + "\n" + student_last_name + "\n" + "you are registered for" + "\n" + COURSE_NAME + "\n" + "!")

# String interpolation with an f-string
print("string interpolation with an f-string example")
print(f"Hello {student_first_name} {student_last_name} you are registered for {COURSE_NAME}!")
