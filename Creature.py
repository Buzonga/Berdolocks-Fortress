class Creature:

    def __init__(self, name, attack_power, armour_class, max_health_points):
        self.name = name
        self.attack_power = attack_power
        self.armour_class = armour_class
        self.max_health_points = max_health_points
        self.current_health_points = max_health_points
        self.is_alive = True

    def show_stats(self):
        print(f"Name: {self.name}")
        print(f"Attack Power: {self.attack_power}d6")
        print(f"Armour Class: {self.armour_class}")
        print(f"Max HP: {self.max_health_points}")
        print(f"Current HP: {self.current_health_points}")