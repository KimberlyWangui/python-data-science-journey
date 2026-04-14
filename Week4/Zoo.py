class Animal(object):
    def __init__(self, name, weight):
        self.name = name
        self.size = None
        self.weight = weight
        self.species = None
        self.foodtype = None
        self.nocturnal = False

    def sleep(self):
        if self.nocturnal:
            print(f"{self.name} sleeps during the day.")
        else:
            print(f"{self.name} sleeps during the night.")

    def eat(self, food):
        if self.food_type == 'omnivore':
            print("{} the {} thinks {} is Yummy!".format(self.name, self.species, food))
        elif (food == 'meat' and self.food_type == "carnivore") or (food == 'plants' and self.food_type == 'herbivore'):
            print("{} the {} thinks {} is Yummy!".format(self.name, self.species, food))
        else:
            print("I don't eat this!")

class Elephant(Animal):
     def __init__(self, name, weight):
        super().__init__(name, weight)
        self.size = 'enormous'
        self.species = 'elephant'
        self.food_type = 'herbivore'
        self.nocturnal = False

class Tiger(Animal):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.size = 'large'
        self.species = 'tiger'
        self.food_type = 'carnivore'
        self.nocturnal = True

class Raccoon(Animal):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.size = 'small'
        self.species = 'raccoon'
        self.food_type = 'omnivore'
        self.nocturnal = True

class Gorilla(Animal):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.size = 'large'
        self.species = 'gorilla'
        self.food_type = 'herbivore'
        self.nocturnal = False

def add_animal_to_zoo(zoo, animal_type, name, weight):
    animal = None
    if animal_type == 'Gorilla':
        animal = Gorilla(name, weight)
    elif animal_type == 'Raccoon':
        animal = Raccoon(name, weight)
    elif animal_type == 'Tiger':
        animal = Tiger(name, weight)
    else:
        animal = Elephant(name, weight)
    
    zoo.append(animal)
    
    return zoo

to_create = [{'Type': 'Elephant', 'name': 'Joe', 'weight': 200}, 
 {'Type': 'Elephant', 'name': 'Tim', 'weight': 220},
 {'Type': 'Raccoon', 'name': 'Dan', 'weight': 30},
 {'Type': 'Raccoon', 'name': 'Roxy', 'weight': 40},
 {'Type': 'Gorilla', 'name': 'Kim', 'weight': 130},
 {'Type': 'Tiger', 'name': 'Bob', 'weight': 70},
 {'Type': 'Tiger', 'name': 'Fred', 'weight': 90},
 {'Type': 'Tiger', 'name': 'Molly', 'weight': 85}]

zoo = []

for animal in to_create:
    zoo = add_animal_to_zoo(zoo, animal['Type'], animal['name'], animal['weight'])

print(zoo)


def feed_animals(zoo, time='Day'):
    for animal in zoo:
        if time == 'Day':
            # CASE: Daytime feeding -- Only feed the animals that aren't nocturnal
            if animal.nocturnal == False:
                # If the animal is a carnivore, feed it "meat".  Otherwise, feed it "plants"
                if animal.food_type == 'carnivore':
                    animal.eat('meat')
                else:
                    animal.eat('plants')
        else:
            # CASE: Night-time feeding -- feed only the nocturnal animals! 
            if animal.nocturnal == True:
                if animal.food_type == 'carnivore':
                    animal.eat('meat')
                else:
                    animal.eat('plants')

feed_animals(zoo, time='Day')
print("\n")
feed_animals(zoo, time='Night')
