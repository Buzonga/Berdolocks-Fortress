class Creature:

    def __init__(self, name, attack_power, armour_class, max_health_points):
        self.name = name
        self.attack_power = attack_power
        self.armour_class = armour_class
        self.max_health_points = max_health_points
        self.current_health_points = max_health_points
        self.is_alive = True

    def show_stats(self):
        print(self.name)
        print(self.attack_power)
        print(self.armour_class)
        print(self.max_health_points)
        print(self.current_health_points)
        print(self.is_alive)