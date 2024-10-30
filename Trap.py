from Dice import Dice

def trap_roll(adventurer):
    if not adventurer.magic_ring:
        print("You walked into a trap!")
        roll = Dice.roll(1)

        damage = 0

        # Trap damage
        if roll in (1, 2, 5):
            damage = Dice.roll(1)
        elif roll == 3:
            damage = Dice.roll(3)
        elif roll == 4:
            damage = Dice.roll(2)

        if roll != 6:
            adventurer.current_health_points -= damage

        if roll == 1:
            print(f"You fell into a trapdoor and took {damage} damage.")
        elif roll == 2:
            print(f"You were hit by a rain of darts and took {damage} damage.")
        elif roll == 3:
            print(f"Acid fell from the roof and you took {damage} damage.")
        elif roll == 4:
            print(f"You were hit by a rain of arrows and took {damage} damage.")
        elif roll == 5:
            print(f"Toxic Gas leaked from the wall and you took {damage} damage.")
        elif roll == 6:
            print("The roof collapses and you die.")
            adventurer.is_alive = False
        if roll != 6 and adventurer.current_health_points <= 0:
            print("You died.")
            adventurer.is_alive = False
        print(f"You have {adventurer.current_health_points} Health Points "
              f"left;")
    else:
        print("The magic ring warns you about a trap! You avoid the trap.")