from Dice import Dice
from Trap import trap_roll
from TreasureChest import treasure_roll

def normal_movement(adventurer):
    roll = Dice.roll(1)
    print(f"You have rolled a {roll}")

    if roll in (2, 5, 6, 8, 9, 10):
        print("You walk into a new section of the dungeon.")
    elif roll == 3:
        trap_roll(adventurer)
    elif roll in (4, 12):
        treasure_roll(adventurer)
    elif roll in (7, 11):
        print("combat")