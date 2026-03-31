# This is the process of checking the data entered and ensuring it matches what the program expects
# Important to avoid being hacked, to maintain data integrity, to handle errors, among others
#age = int(input("Enter you age: "))
#print("In five years, you will be", age + 5)

# Adding validation using if:
# "Please enter an"
# age = int(input("Enter you age: "))
# if 18 < age <100:
#if age < 18:
#     print("Age cannot be less than 18")
# elif age > 120:
#     print("Age cannot be greater than 120")
# else:
#     print("Your age is:", age)

# def getValid():
#     while True:
#         age = int(input("Enter you age: "))
#         if age.isdigit(): # ensures we don't allow non-numerical values
#             if age < 18:
#              print("Age cannot be less than 18") 
#             elif age > 120:
#                 print("Age cannot be greater than 120")
#             else:
#                 print("Your age is:", age) 
#                 break
#         else:
#             print("Please enter a numerical value")
# getValid()

# Core Validation Techniques:
# type checking: Checks the types of variables that we have ie. integers, strings

# Checking for an int:
# value = input("Enter a value: ")
# # isinstance() - checks the type of variable
# if isinstance(value, int):
#     print("An integer")
# else:
#     print("Not an integer")
# print("Your value is:", value)

# Using range checking. Check that the score is within a range (0-100):
score = float(input("Enter score: "))
if isinstance(score, float): # add brackets if we have 2
    if score < 0 or score > 100: # only use range when working with whole numbers
        print("Score is invalid")
    else:
        print("Score is valid")
else:
    print("Not a number")
    # if not isinstance(value, int(range(0,100))): # using notisinstance to make sure it's within the range
    # if value < 0:
    #     print("You entered a negative integer")
    # elif value > 100:
    #     print("You entered a value greater than 100")
    # else:
    #     print("Not an integer")
# isinstance only checks the data type

# Regex 
score = input("Enter your score: ")

try:
    score = float(score) if "." in score else int(score) 
except ValueError:
    print("Please enter a valid number")
    score = None

if isinstance(score, (int, float)):
    if 1 <= score <= 100:
        print("Valid score within range:", score)
    else:
        print("Score out of range, must be between 1 and 100")
else:
    print("Not a valid score")

# Create a fn that takes in a score, checks whether it is an integer between 0 and 100. Ask user to add the scores and use the score.
def validate_score(score):
    try:
        score = float(score) if "." in score else int(score)
    except ValueError:
        print("Please enter a valid number")
        return None

    if isinstance(score, (int, float)):
        if 0 <= score <= 100:
            print("Valid score within range:", score)
            return score
        else:
            print("Score out of range, must be between 0 and 100")
            return None
    else:
        print("Not a valid score")
        return None
    
score_input = input("Enter your score: ")
validated_score = validate_score(score_input)

        