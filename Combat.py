from Dice import Dice
from Monster import Monster
def combat_start(adventurer):
    combat = True
    monster = Monster(Dice.roll(1))

    print(f"You found a {monster.name}! The combat begins.\n"
          f"\nRolling initiative.\n")

    adventurer_initiative = Dice.roll(1)
    monster_initiative = Dice.roll(1)

    print(f"{adventurer.name}'s initiative: {adventurer_initiative}")
    print(f"{monster.name}'s initiative: {monster_initiative}\n")

    cont()

    if monster_initiative > adventurer_initiative:
        print(f"The {monster.name} attacks.")
        monster.attack(adventurer)
        print(f"You have {adventurer.current_health_points} Health Points "
              f"left.")
        if not adventurer.is_alive:
            print("You died.")
            combat = False
        cont()
    while combat:
        print("You attack")
        adventurer.attack(monster)
        if not monster.is_alive:
            print(f"The {monster.name} died.")
            combat = False
        cont()
        if monster.is_alive:
            print(f"The {monster.name} attacks.")
            monster.attack(adventurer)
            print(f"You have {adventurer.current_health_points} Health Points "
                  f"left.")
            if not adventurer.is_alive:
                print("You died.")
                combat = False
        cont()

def cont():
    op = input("Type 1 to continue")
    while op != "1":
        op = input("Type 1 to continue")
