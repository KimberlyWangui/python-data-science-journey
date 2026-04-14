# Define the base class
class Guitarist(object):
    def __init__(self, name):
        self.name = name
        self.role = "Guitarist"
        self.instrument_type = "Stringed Instrument"

    def tune_instrument(self):
        print("Tune the Strings")

    def practice(self):
        print("Strumming the old 6 string!")

    def perform(self):
        print("Hello, New York!")

# Pass the base class as arugment to the child class for inheritance
class Bass_Guitarist(Guitarist):
    def __init__(self, name):
        super().__init__(name) # Call the parent class constructor
        self.role = "Bass Guitarist"
        self.string_type = "bass"

    def practice(self):
        print("I play the Seinfeld theme song when I practice!")

    def perform(self):
        super().perform() # Call the parent class method
        print("This is the bass line")


george = Guitarist("George")
paul = Bass_Guitarist("Paul")
# print(george.instrument_type)
# print(paul.instrument_type)
# print("---")
# george.tune_instrument()
# paul.tune_instrument()
# print("---")
# george.practice()
# paul.practice()
# print("---")
# george.perform()
# paul.perform()

#print(george.string_type) # This will raise an error because the base class does not have this attribute
print(paul.string_type) # This will print "bass" because the child class has this attribute

george.practice()
paul.practice()

    