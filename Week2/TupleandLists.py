# Tuples - created using () function and are immutable (cannot be changed after creation)

coordinates = (10, 20)
students = ("Alice",20, "Computer Science", "Bob", 22, "Mathematics", "Charlie", 21, "Physics")
empty_tuple = ()
single_tuple = (5,) # Note the comma, without it, it would be considered an integer

# Accessing tuple elements
#print(students[0]) 
#print(students[1])
print(students[0:7]) # Slicing the tuple
print(students[:2]) # Accessing the first two elements
print(students[2:]) # Accessing from the third element to the end



# Lists: ordered and mutable (can be changed after creation) created using [] function
# Most commonly used data structure in Python
 # scores = [] # Empty list
name = ["Alice", "Bob", "Charlie", "David", "Eve"] # List of names
values = [10, 20, 30, 40, 50] # List of numbers
mixed_list = ["Alice", 20, "Computer Science", "Bob", 22, "Mathematics", "Charlie", 21, "Physics"] # List with mixed data types
numbers = list(range(1, 6)) # List of numbers from 1 to 5

numbers = list(range(1, 6))
print(numbers)

scores = [85, 90, 78, 92, 88]
print(scores[0]) # Accessing the first element
print(scores[1]) # Accessing the second element
print(scores[0:5]) # Slicing the list
print(scores[:3]) # Accessing the first three elements

# Modifying a list
fruits = ["Apple", "Banana", "Cherry"]
print(fruits[1])
fruits.append("Apricot") # Adding a new element to the end of the list
fruits.insert(0, "Pineapple") # Inserting an element at a specific position
fruits[1] = "Blueberry" # Modifying the second element
print(fruits)

# removing elements from a list
fruits.remove("Cherry") # Removing an element by value
print(fruits)

# removes and returns the last element
last_fruit = fruits.pop() # Removing the last element and storing it in a variable
print(last_fruit)

# removes and returns the element at a specific index
first_fruit = fruits.pop(1) # Removing the first element and storing it in a variable
print(first_fruit)

del fruits[0] # Removing the first element using del keyword
print(fruits)

# sort, sortreverse, len(), count()

# list comprehension - a concise way to create lists
scores = [85, 90, 78, 92, 88]
passing = []

for score in scores:
    if score >= 80:
        passing.append(score)
print(passing)

passing = [score for score in scores if score >= 80]
print(passing)



cars = ["Toyota", "Honda", "Ford", "BMW", "Audi"]
print("Cars:", cars)
uppercase_cars = [car.upper() for car in cars]
print("Uppercase Cars:", uppercase_cars)


colors = ["red", "green", "blue", "yellow", "purple"]

# Sorting the list in ascending order
colors.sort()
print("Sorted Colors:", colors)

# Sorting the list in descending order
colors.sort(reverse=True)
print("Sorted Colors (Descending):", colors)

# Getting the length of the list
print("Number of colors:", len(colors))

# Getting the count of a specific element in the list
print("Count of 'red':", colors.count("red"))

colors.reverse() # Reversing the order of the list
print("Reversed Colors:", colors)