# Regex functions:
# - re.match() - matches a pattern at the beginning of the string
# - re.search() - searches for a pattern anywhere in the string
# - re.fullmatch() - matches the entire string against a pattern
# - re.findall() - finds all occurrences of a pattern in the string

# Regex building blocks:
# . (wildcard) - matches any character except a newline
# \d - matches any digit (0-9)
# \D - matches any non-digit
# \w - matches any word characters and underscore(letters/digits/_).
# \W - matches any non-word character
# \s - matches any whitespace character, tab or newline
# \S - matches any non-whitespace character
# [abc] (character class) - matches any one of the characters a, b, or c
# [^abc] (negated character class) - matches any character except a, b, or c
# [a-z] (character range) - matches any one character from a to z
# [A-Z] (character range) - matches any one character from A to Z(uppercase)
# ^ (start anchor) - matches the start of the string
# $ (end anchor) - matches the end of the string
# * (Zero or more) - matches 0 or more occurrences of the preceding element
# + (One or more) - matches 1 or more occurrences of the preceding element
# ? (Optional) - repeats previous character 0 or 1 time
# {n} (Exactly n) - matches exactly n occurrences of the preceding element
# {n,m} (Between n and m) - matches between n and m occurrences of the preceding element
# \b (Word boundary) - matches the position between a word character and a non-word character
# \n (Newline) - matches a newline character


# Example usage of regex functions and building blocks

import re

# check if a string contains only digits
pattern = r'\d+'
string1 = "23456"
string2 = "Hello"
string3 = "123abc"
string4 = ""

print(re.fullmatch(pattern, string1)) 
print(re.fullmatch(pattern, string2))  
print(re.fullmatch(pattern, string3))  
print(re.fullmatch(pattern, string4))

# Matching of phone numbers that start with country code +254 followed by 9 digits
phone_pattern = r'^\+254\d{9}$'
phone1 = "+254712345678"
phone2 = "0712345678"
phone3 = "+25412345678"

print(re.fullmatch(phone_pattern, phone1))
print(re.fullmatch(phone_pattern, phone2))
print(re.fullmatch(phone_pattern, phone3))


# Emample 2
# find the first phone number in a string
text = "call us at 0712345678 or 0111234567"
pattern = r'\d{10}'
print(re.search(pattern, text))

# How to return both numbers in the string?
print(re.findall(pattern, text))


# example 3
text2 = "Call us at 0712-345-678 or 0111-234-567"
pattern2 = r'\d{4}-\d{3}-\d{3}'
print(re.findall(pattern2, text2))

text3 = ["0712-345-678", "0712 345 678", "0111234567", "0712/345/678"]
pattern3 = r'^\d{4}[-\s/]*\d{3}[-\s/]*\d{3}$'

#print([re.findall(pattern3, number) for number in text3])

for number in text3:
    if re.fullmatch(pattern3, number):
        print(f"{number} is a valid phone number.")
    else:
        print(f"{number} is not a valid phone number.")