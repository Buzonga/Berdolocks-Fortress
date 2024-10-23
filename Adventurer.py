from Creature import Creature

class Adventurer:

    def __init__(self, name, attack_power, armour_class, max_health_points):
        super().__init__(name, attack_power, armour_class, max_health_points)
        self.current_health_points = max_health_points
        self.is_alive = True
        self.potion_number = 0
        self.gold_coins = 0
        self.magic_ring = False
        self.magic_armour = False
        self.armour = "Chainmail and Wood Shield"
        self.sword = "Sword"