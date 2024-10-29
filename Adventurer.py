from Creature import Creature
from Dice import Dice
from CreateName import create_name
class Adventurer(Creature):

    def __init__(self):
        self.name = create_name()
        self.attack_power = 2
        self.armour_class = 7
        self.max_health_points = Dice.roll(2)
        self.current_health_points = self.max_health_points
        self.is_alive = True
        self.potion_number = 0
        self.gold_coins = 0
        self.magic_ring = False
        self.magic_armour = False
        self.armour = "Chainmail and Wood Shield"
        self.sword = "Sword"

    def show_stats(self):
        super().show_stats()
        print(f"Potions: {self.potion_number}")
        print(f"Gold Coins: {self.gold_coins}")
        print(f"Armour: {self.armour}")
        print(f"Sword: {self.sword}")
        if self.magic_ring:
            print("Magic Ring")