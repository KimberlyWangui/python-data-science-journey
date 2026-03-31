import re

# Validate the customer email address
def validate_email(email):
    if not email:
        raise ValueError("Email cannot be empty.")
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        raise ValueError("Invalid email format.")
    
# Validate the customer's driver's license number - it should be alphanumeric characters
def validate_drivers_license(license_number):
    if not license_number:
        raise ValueError("Driver's license number cannot be empty.")
    if not license_number.isalnum():
        raise ValueError("Driver's license number can only contain alphanumeric characters.")
    
# Validate the customer's rental duration days - it should be a positive integer
def validate_rental_duration(days):
    if not days.isdigit():
        raise ValueError("Rental duration must be a positive integer.")
    days = int(days)
    if days <= 0:
        raise ValueError("Rental duration must be a positive integer.")

# User input
email = input("Enter your email: ")
drivers_license = input("Enter your driver's license number: ")
rental_duration = input("Enter rental duration in days: ")

# Validate inputs
try:
    validate_email(email)
    validate_drivers_license(drivers_license)
    validate_rental_duration(rental_duration)
    print("All inputs are valid. You can proceed with the car rental process.")
except ValueError as e:
    print("Input validation error:", str(e))