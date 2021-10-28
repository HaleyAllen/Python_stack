
import ninja

class LargePet:
    def __init__(self, name , type , tricks ):
        self.name = name 
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100
    
    def sleep(self):# - increases the pets energy by 25
        self.energy += 25
        print("Energy=", self.energy)
        return self
    def eat(self):# - increases the pet's energy by 5 & health by 10
        self.energy += 5
        self.health += 10
        print("Energy=", self.energy)
        print("Health=", self.health)
        return self
    def play(self):# - increases the pet's health by 5
        self.health += 5
        print("Health=", self.health)
        return self
    def noise(self):# - prints out the pet's sound
        print("bark bark!")
        self.health += 10
        print("Health=", self.health)
        return self

class SmallPet(LargePet):
    def __init__(self, name , type , tricks, habitat):
        super().__init__(name, type, tricks)
        self.habitat = habitat
        self.health = 100
        self.energy = 100
    
    def sleep(self):
        super().sleep(self)
        return self
    def eat(self):
        super().eat(self)
        return self
    def play(self):
        super().play(self)
        return self
    def noise(self):
        super().noise(self)
        return self

pumpkin = LargePet("Pumpkin", "Dog", "Smiles")
max = SmallPet("Max", "Cat", "None", "Where ever he wants")
christian = ninja.Ninja("Christian", "Allen", "Bully Sticks", "Nutra Nuggets", max)

christian.feed(max).walk(max).bathe(max)
