from Creature import Creature

class Monster(Creature):

    def __init__(self, roll):
        if roll == 1:
            self.create_giant_spider()
        elif roll == 2:
            self.create_undead()
        elif roll == 3:
            self.create_ghost()
        elif roll == 4:
            self.create_orc()
        elif roll == 5:
            self.create_troll()
        elif roll == 6:
            self.create_chaos_warrior()
        self.current_health_points = self.max_health_points
        self.is_alive = True

    def create_giant_spider(self):
        self.name = "Giant Spider"
        self.attack_power = 3
        self.armour_class = 7
        self.max_health_points = 20

    def create_undead(self):
        self.name = "Undead"
        self.attack_power = 2
        self.armour_class = 5
        self.max_health_points = 8

    def create_ghost(self):
        self.name = "Ghost"
        self.attack_power = 3
        self.armour_class = 9
        self.max_health_points = 14

    def create_orc(self):
        self.name = "Orc"
        self.attack_power = 2
        self.armour_class = 6
        self.max_health_points = 10

    def create_troll(self):
        self.name = "Troll"
        self.attack_power = 3
        self.armour_class = 8
        self.max_health_points = 18

    def create_chaos_warrior(self):
        self.name = "Chaos Warrior"
        self.attack_power = 3
        self.armour_class = 9
        self.max_health_points = 16