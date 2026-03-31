# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

from hashlib import new


students = {
    "name": "John",
    "age": 25,
    "student_id": "12345",
    "course": "Data Science",
    "gender": "Male"
}

print(students)

# Accessing values in a dictionary
print(students["name"], students["course"])
print(f"{students['name']} is enrolled in {students['course']} course.")
print(students["age"])

# get() method to access values - it returns None if the key does not exist
print(students.get("course"))
print(students.get("grade"))  # This will return None

print(students.keys())  # Returns all the keys in the dictionary
print(students.values())  # Returns all the values in the dictionary
print(students.items())  # Returns all the key-value pairs in the dictionary

# Modifying values in a dictionary
students.update({"name": "Dave"})
print(students["name"])
students.update({"age": 30})
print(students["age"])

students["course"] = "Machine Learning"
print(students["course"])

print(students)

students.pop("gender")  # Removes the key "gender" and its associated value
print(students)

del students["age"]  # Removes the key "age" and its associated value
print(students)

# Copying a dictionary
students_copy = students.copy()
# You can also use the dict() constructor to create a copy of the dictionary
# students_copy = dict(students)
print(students_copy)

# Add a new key-value pair to the copied dictionary
students_copy["grade"] = "A"
print(students_copy)

students_copy.update({"height": "6ft"})
print(students_copy)

# Removing a key-value pair from the copied dictionary
students_copy.popitem()  # Removes the last inserted key-value pair
print(students_copy)

# Loops with dictionaries
for key in students:
    print(f"These are the keys: {key}")  # Prints the keys of the dictionary

for key, value in students.items():
    print(f"These are the key-value pairs: {key}: {value}")  # Prints the key-value pairs of the dictionary

# Printing the values of the dictionary
for value in students.values():
    print(f"The values: {value}")  # Prints the values of the dictionary


# Nested dictionaries
student_details = {
    "student1": {
        "name": "Alice",
        "age": 22,
        "course": "Computer Science"
    },
    "student2": {
        "name": "Bob",
        "age": 24,
        "course": "Mathematics"
    }
}

print(student_details["student1"]["name"], student_details["student1"]["age"])  # Output: Alice 22
print(student_details["student2"]["course"])  # Output: Mathematics

# You can also use the get() method to access values in a nested dictionary
print(student_details.get("student1").get("age"))  # Output: 22

'''# Looping through a nested dictionary
for student, details in student_details.items():
    print(f"{student}:")
    for key, value in details.items():
        print(f"  {key}: {value}")

newstudent_details = student_details.fromkeys(
    ["student3", "student4"], 
    {"name": "Unknown", "age": 0, "course": "None"})
print(newstudent_details)

student_details.update(newstudent_details)
print(student_details)
'''

std = [ 
    {
        "name": "John",
        "age": 25,
        "student_id": "12345",
        "course": "Data Science",
    },
    {
        "name": "Alice",
        "age": 22,
        "student_id": "67890",
        "course": "Computer Science",
    },
    {
        "name": "Bob",
        "age": 24,
        "student_id": "11223",
        "course": "Mathematics",
    },
    {
        "name": "Dave",
        "age": 30,
        "student_id": "44556",
        "course": "Machine Learning",
    },
    {
        "name": "Eve",
        "age": 28,
        "student_id": "77889",
        "course": "Artificial Intelligence",
    }
]

'''
print(std[0]["name"], std[0]["age"])  # Output: John 25
print(std[1]["name"], std[1]["age"])  # Output: Alice 22
print(std[2]["name"], std[2]["age"])  # Output: Bob 24
'''
# looping to return the names and ages of the students
for student in std:
    print(f"{student['name']} is {student['age']} years old.")