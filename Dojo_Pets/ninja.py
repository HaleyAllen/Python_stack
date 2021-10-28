
import pets

class Ninja:
    def __init__(self, first_name , last_name , treats , pet_food , pet ):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    
    def walk(self, pet): # walks the ninja's pet invoking the pet play() method
        pets.LargePet.play(pet)
        return self

    def feed(self, pet): # - feeds the ninja's pet invoking the pet eat() method
        pets.LargePet.eat(pet)
        return self
    
    def bathe(self, pet):# - cleans the ninja's pet invoking the pet noise() method
        pets.LargePet.noise(pet)
        return self
