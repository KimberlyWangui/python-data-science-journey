# Creating Strings
# Strings are created by enclosing characters in quotes. Python supports both single and double quotes for string literals.
# Example:
name = "Kimberly"
city = "New York"

name = 'Kimberly'
city = 'New York'
phone = '123-456-7890'

print(type(name))  

# Indexing in strings
word = "Moringa"
print(word[0])  
print(word[-1])  

# Slicing in strings
print(word[0:4])  # Output: 'Mori'
print(word[2:5])  # Output: 'rin'
print(word[:4])   # Output: 'Mori'
print(word[3:])   # Output: 'inga'
print(word[:])    # Output: 'Moringa'

message = "Hello, World!"
print(message[7:])
print(message[-5:])
print(message[::-1])  # Output: '!dlroW ,olleH' 

print(message[::-5]) # Output: '!oH' (reverses the string and takes every 5th character)

# String Concatenation
first_name = "Kim"
last_name = "Kui"

full_name = "My name is " + first_name + " " + last_name + "."
print(full_name)  

# Stripping
greeting = "   Hello, World!   " # String with leading and trailing whitespace
print(greeting.strip())  # Removes leading and trailing whitespace
print(greeting.lstrip()) # Removes leading whitespace
print(greeting.rstrip()) # Removes trailing whitespace

text1 = 'Moringa#'
print(text1)
print(text1.strip('#'))  # Output: 'Moringa' (removes the '#' character from both ends)

text4 = 'Moringa School'
print(text4)
print(text4.strip('School'))  # Output: 'Moringa ' (removes 'School' from the end, but not from the beginning)
print(text4.strip('Moringa '))  # Output: ' School' (removes 'Moringa' from the beginning, but not from the end)

print(text4.replace(' ', ''))  # Output: 'MoringaSchool' (removes all spaces from the string)

print(''.join(text4.split()))  # Output: 'MoringaSchool' (removes all spaces from the string)


text5 = "Moringa School"
print(text5.split())  # Output: ['Moringa', 'School'] (splits the string into a list of words)

date1 = "24-03-2026"
date2 = "24/03/2026"
print(date1.split("-"))  # Output: ['24', '03', '2026'] (splits the date string into a list using '-' as the delimiter)
print(date2.split("/"))  # Output: ['24', '03', '2026'] (splits the date string into a list using '/' as the delimiter)

# split splits white space by default, but you can specify a different delimiter if needed. 
# In the case of date strings, you can use the appropriate delimiter to split the string into its components (day, month, year).