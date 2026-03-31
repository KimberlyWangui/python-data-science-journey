password = input("Enter your password: ")
minimum_length = 8

# Checking the length of the password
password_length = len(password)

if password_length < minimum_length:
    print(f"Password is too short. It should be at least {minimum_length} characters long.")
else:
    print(f"Password length is sufficient. It meets the minimum requirement of {minimum_length} characters.")


# Validating character types
has_uppercase = False
has_lowercase = False
has_number = False
has_symbol = False

for char in password:
    if char.isupper():
        has_uppercase = True
    elif char.islower():
        has_lowercase = True
    elif char.isdigit(): # Check for numbers
        has_number = True
    elif not char.isalnum():  # Check for symbols (non-alphanumeric characters)
        has_symbol = True

# # Printing the results
# print(f"Contains uppercase: {has_uppercase}")
# print(f"Contains lowercase: {has_lowercase}")
# print(f"Contains number: {has_number}")
# print(f"Contains symbol: {has_symbol}")

# Evaluating the password strength
if has_uppercase and has_lowercase and has_number and has_symbol:
    print("Congratulations! Your password is strong.")
else:
    print("Password is weak. Consider including:")
    if not has_uppercase:
        print("- Uppercase letters (A-Z)")
    if not has_lowercase:
        print("- Lowercase letters (a-z)")
    if not has_number:
        print("- Numbers (0-9)")
    if not has_symbol:
        print("- Symbols (e.g., !, @, #, $)")