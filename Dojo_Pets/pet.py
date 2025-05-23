class Pet:
    def __init__(self, name, petType, tricks):
        self.name= name
        self.petType= petType
        self.tricks=tricks
        self.health=100
        self.energy=50
    def sleep(self):
        self.energy += 25
        print(f"{self.name} is sleeping now!! Energy : {self.energy}")
    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name} is eating. Health:{self.health} Energy: {self.energy}")
    def play(self):
        self.health += 5
        print(f"{self.name} is playing!! Health: {self.health}")
    def noise(self,sound):
        print(f"{self.name} is making the sound: {sound}")


if __name__=="__main__":
    class Cat(Pet):
        def __init__(self,name,tricks):
            super().__init__(name,"cat",tricks)
        def noise(self):
            super().noise("meow")

    cat= Cat("Luna","jump")
    cat.play()
    cat.noise()

