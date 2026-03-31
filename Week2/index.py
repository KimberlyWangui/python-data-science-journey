# no parameter, no return value
def print_welcome():
    print("Welcome to the Python for Data Science!")

print_welcome()

# parameter and return value
"square each number and return a list"
def square(*numbers):
    return [number * number for number in numbers]


print(square(5, 4, 3, 2, 1))

result = square(10)
print(result)


# Default parameter value
def greet(name, language="English"):
    if language == "English":
        print(f"Hello, {name}!")
    elif language == "Spanish":
        print(f"Hola, {name}!")
    elif language == "French":
        print(f"Bonjour, {name}!")
    else:
        print(f"Hello, {name}! (Language not supported)")

greet("Alice")
greet("Bob", "Spanish")
greet("Charlie", "French")
greet("Dave", "German")

# create a function within a function, the first function defines temperature validations. 
# The next function uses the first function to classify the temperature as "Cold", "Warm", or "Hot".

def validate_temperature(temp):
    if temp < 0:
        return "Temperature is below absolute zero!"
    elif temp > 100:
        return "Temperature is above boiling point!"
    else:
        return "Temperature is within the valid range."
    
def classify_temperature(temp):
    validation_message = validate_temperature(temp)
    print(validation_message)
    
    if temp < 15:
        return "Cold"
    elif 15 <= temp < 25:
        return "Warm"
    else:
        return "Hot"
    
temperature = 22
classification = classify_temperature(temperature)
print(f"The temperature of {temperature}°C is classified as: {classification}")