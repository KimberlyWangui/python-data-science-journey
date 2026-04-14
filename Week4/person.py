class Person():

    def introduce(self):
        return f'Hi, my name is {self.name}. It is a pleasure to meet you!'
    
    def say_hello(self):
        return 'Hi, how are you?'
    
    def eat_sandwhich(self):
        if (self.hungry):
            self.relieve_hunger()
            return "Wow, that really hit the spot! I am so full, but more importantly, I'm not hangry anymore!"
        else:
            return "Oh, I don't think I can eat another bite. Thank you, though!"
        
    def relieve_hunger(self):
        print("Hunger is being relieved")
        self.hungry = False
    
    def say_hello_and_weather(self, weather_pattern):
        return f"Hi, my name is {self.name}! What wildly {weather_pattern} weather we're having, right?!"
    
    def happy_birthday(self):
        self.age += 1
        return f"Happy birthday {self.name}! You are now {self.age} years old!"

gail = Person()
gail.name = 'Gail'
gail.age = 29
gail.hungry = False
the_snail = Person()
the_snail.name = 'The Snail'
the_snail.hungry = True
print('1.', gail.introduce())
print('2.', the_snail.introduce())
print('3.', gail.say_hello_and_weather('sunny'))
print('4.', gail.age)
print('5.', gail.happy_birthday())
print('6.', gail.eat_sandwhich())
print('7.', the_snail.eat_sandwhich())