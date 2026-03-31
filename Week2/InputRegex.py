import re

# Validating name
def validate_name(name):
    if not name:
        raise ValueError("Name cannot be empty.")
    if not re.match(r'^[A-Za-z ]+$', name):
        raise ValueError("Name can only contain letters and spaces.")
    

# validating the age
def validate_age(age):
    if not age.isdigit():
        raise ValueError("Age must be a positive integer.")
    age = int(age)
    if age <= 0:
        raise ValueError("Age must be a positive integer.")
    
# validating email
def validate_email(email):
    if not email:
        raise ValueError("Email cannot be empty.")
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        raise ValueError("Invalid email format.")
    
# User input
name = input("Enter your name: ")
age = input("Enter your age: ")
email = input("Enter your email: ")

# Validate inputs
try:
    validate_name(name)
    validate_age(age)
    validate_email(email)
    print("All inputs are valid.")
except ValueError as e:
    print("Input validation error:", str(e))

