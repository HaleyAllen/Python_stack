
# 1. create class for game
# 2. create they attributes for game
# 3. start make methods


import random

class Game:
    def init(self, ):
        self.is_running = True

    def play(self, p1, p2):
        while self.is_running:
            if p1.health > 0 and p2.health > 0:
                p1.attack(p2)
            else:
                self.is_running = False



class Character:
    def init(self, parent, name, attack_strength=20, defense_strength=30, health=100):
        self.parent = Game
        self.name = name
        self.attack_strength = attack_strength
        self.defense_strength = defense_strength
        self.health = health

    def info(self):
        print(f'{self.name}')
        print(f'Health: {self.health}')
        print(f'Attack: {self.attack_strength}')
        print(f'Defense: {self.defense_strength}')
        return self

    def attack(self, attackee:object):
        attack_roll= random.randint(0, self.attack_strength)
        # print(attack_roll)
        # attackee.health -= attack_roll
        attackee.defense(self, attack_roll)
        return self

    def defense(self,attacker:object, attack_roll):
        defense_roll = random.randint(0, self.defense_strength)
        print(f'{attacker.name} attacking with {attack_roll} damage! {self.name} defending with {defense_roll} defense!')
        actual_attack = attack_roll - defense_roll
        print(actual_attack)
        self.health -= actual_attack
        print(self.health)
        return self

    # def battle(self, attacker:object, attackee:object):
    #     self.attack() - self.defense()
    #     return self
class Instructor(Character):
    def init(self, name, attack_strength=75, defense_strength=60, health=200):
        super().init(name, attack_strength, defense_strength, health)

class Teacher_assistant(Character):
    def init(self, name, attack_strength=40, defense_strength=50, health=100):
        super().init(name, attack_strength, defense_strength, health)

tyler = Instructor(('Tyler'))
tyler.info()

christian = Teacher_assistant(('Christian'))
christian.info()


game = Game()

game.play(tyler, christian)
christian.info()