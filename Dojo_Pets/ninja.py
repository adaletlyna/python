from pet import Pet
class Ninja ():
    def __init__(self,first_name,last_name,treats,pet_food, pet):#composition
        self.first_name= first_name
        self.last_name= last_name
        self.pet= pet
        self.treats= treats
        self.pet_food= pet_food
    def walk(self):
        print(f"{self.first_name} is walking {self.pet.name}")
        self.pet.play()
        return self
    def feed (self):
        print(f"{self.first_name} is feeding {self.pet.name}")
        self.pet.eat()
        return self

    def bathe(self,sound):
        print(f"{self.first_name} is bathing {self.pet.name}")
        self.pet.noise(sound)
        return self

dog=Pet("Rex","dog",["run","jump"])
ninja= Ninja("Mike", "Doe","fdvf","meat",dog)
ninja.walk().feed().bathe("woolf")


        
