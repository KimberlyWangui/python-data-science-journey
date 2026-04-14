class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"
    
    def speak(self, sound):
        return f"{self.name} says {sound}"
    

# Creating instances
dog1 = Dog("Buddy", 5)
print(dog1.description())  # Output: Buddy is 5 years old
print(dog1.speak("Woof"))  # Output: Buddy says Woof
dog2 = Dog("Max", 3)
print(dog2.description())  # Output: Max is 3 years old
print(dog2.speak("Bark"))  # Output: Max says Bark

# # Accessing class attribute
print(dog1.species)  # Output: Canis familiaris
print(dog2.species)  # Output: Canis familiaris
print(Dog.species)   # Output: Canis familiaris

# Modifying instance attribute
dog1.age = 6
print(dog1.age)  # Output: 6
print(dog2.age)  # Output: 3

# Modifying class attribute
Dog.species = "Canis lupus familiaris"
print(dog1.species)  # Output: Canis lupus familiaris
print(dog2.species)  # Output: Canis lupus familiaris

# class Dog:
    
#     def bark(self):
#         return 'I am actually going to bark this time. bark!'
        
#     def who_am_i(self):
#         return self


# fido = Dog()
# print("1.", fido.who_am_i())
# print("2.", fido)