# import re

# name = input("Enter your name: ")
# email = input("Enter your email: ")
# date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")

# # Check if the name contains only letters and spaces
# def validate_name(name):
#     if re.fullmatch(r"^(?=.*[A-Za-z])[A-Za-z ]+$", name):
#         print("Valid name:", name)
#         return name
#     else:
#         print("Invalid name. Please enter a name containing only letters and spaces.")
#         return None
    
# # Checks if the email is not empty and follows a basic email pattern
# def validate_email(email):
#     if re.fullmatch(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
#         print("Valid email:", email)
#         return email
#     else:
#         print("Invalid email. Please enter a valid email address.")
#         return None
    
# # Checks if the date of birth is in the format YYYY-MM-DD and is a valid date
# def validate_date_of_birth(date_of_birth):
#     if re.fullmatch(r"^\d{4}-\d{2}-\d{2}$", date_of_birth):
#         print("Valid date of birth:", date_of_birth)
#         return date_of_birth
#     else:
#         print("Invalid date of birth. Please enter a date in the format YYYY-MM-DD.")
#         return None
    
# validate_name(name)
# validate_email(email)
# validate_date_of_birth(date_of_birth)

import re
from datetime import datetime

def validate_name(name):
    if not name:
        raise ValueError("Name cannot be empty.")
    if not re.match(r'^[A-Za-z ]+$', name):
        raise ValueError("Name can only contain letters and spaces.")

def validate_email(email):
    if not email:
        raise ValueError("Email cannot be empty.")
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        raise ValueError("Invalid email format.")

def validate_dob(dob):
    if not dob:
        raise ValueError("Date of birth cannot be empty.")
    try:
        datetime.strptime(dob, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

# Student registration
name = input("Enter your name: ")
email = input("Enter your email address: ")
dob = input("Enter your date of birth (YYYY-MM-DD): ")

try:
    validate_name(name)
    validate_email(email)
    validate_dob(dob)
    
    # If all validations pass, store the data in the database
    print("Student registration successful!")
    # Code to store the data in the database goes here
    
except ValueError as e:
    print(f"Error: {str(e)}")