from Creature import Creature

class Monster(Creature):

    def __init__(self, name, attack_power, armour_class, max_health_points):
        super().__init__(name, attack_power, armour_class, max_health_points)
        self.current_health_points = max_health_points
        self.is_alive = True