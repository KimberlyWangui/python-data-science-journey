# Openning a file
file = open("text.txt", "r")

# Read the file
content = file.read()
print(content)

# write the file 
file = open("text.txt", "w")
content = file.write("This is a new line of text.")
file = open("text.txt", "r")
content = file.read()
print(content)

# Writing to the file again - overwrites the existing content
file = open("text.txt", "w")
content = file.write("This is another line of text.")
file = open("text.txt", "r")
content = file.read()
print(content)

# Appending to the file - adds to the existing content
file = open("text.txt", "a")
content = file.write("\nThis line is appended to the file.")
file = open("text.txt", "r")
content =file.read()
print(content)

file = open("text.txt", "a")
content = file.write("\nThe additional line is appended to the file.")
file = open("text.txt", "r")
content =file.readline() # Reads only the first line of the file
print(content)

file.close()
