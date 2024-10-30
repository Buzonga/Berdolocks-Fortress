import Combat
from Combat import combat_start
from Dice import Dice
from Trap import trap_roll
from TreasureChest import treasure_roll

def normal_movement(adventurer):
    roll = Dice.roll(2)
    print(f"You have rolled a {roll}")

    if roll in (2, 5, 6, 8, 9, 10):
        print("You walk into a new section of the dungeon.")
    elif roll == 3:
        trap_roll(adventurer)
    elif roll in (4, 12):
        treasure_roll(adventurer)
    elif roll in (7, 11):
        Combat.combat_start(adventurer)

def escape_movement(adventurer):
    roll = Dice.roll(2)
    print(f"You have rolled a {roll}\n")

    if roll == 1:
        print("You keep walking, but someone found you.")
        combat_start(adventurer)
    elif roll == 2:
        print("You were the only one to find the escape from this infernal "
              "place! You can now tell the terrible adventures that you lived"
              "in the Berdlock's Fortress")
    elif roll == 3:
        print("You fell into a hole in the ground and hurt yourself. You lost 1 "
              "Health Point.")
        adventurer.current_health_points -= 1
    elif roll == 4:
        print("You were approaching an exit, but an enormous boulder falls "
              "and blocks the way out.")
    elif roll == 5:
        print("A skeleton of an ancient adventurer points to a possible exit "
              "of the dungeon. If tou roll a pair you are free from the "
              "Berdolock's Fortress.")
        escape_roll = Dice.roll(1)
        if escape_roll % 2 == 0:
            print("You escaped the dungeon!")
            adventurer.is_alive = False
        else:
            print("You didn't escape. You start to walk again.")
    elif roll == 6:
        print("Despair and hunger takes control of you. You wandered for days"
              " without stop and still the exit didn't appear.\n"
              "\n"
              "If you roll a 1, you will escape, else, you were just another"
              " victim of the dungeon.")
        desperate_roll = Dice.roll(1)
        if desperate_roll == 1:
            print("You have escaped!")
        else:
            print("You were just another victim of the dungeon.")
        adventurer.is_alive = False