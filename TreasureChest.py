from Dice import Dice

def treasure_roll(adventurer):

    roll = Dice.roll(1)
    # 1 magic sword 2 health potion 3ring trap 4 magic armour 5 gold coins 6
    # cursed item
    if roll == 1:
        sword = adventurer.sword
        print("You found a treasure with a Magic Sword inside!")
        if sword == "Sword":
            print("You trade your old Sword for the Magic Sword, your damage "
                  "now is 3d6")
            sword = "Magic Sword"
            adventurer.attack_power = 3
        else:
            print("You already have a Magic Sword. Leaving this one behind.")
    elif roll == 2:
        print("You have found a Health Potion!")
        potions = adventurer.potion_number
        if potions <= 4:
            potions += 1
            s = ""
            if potions == 0:
                s = "s"
            print(f"You grab the potion. You now have {potions}"
                  f" potion{s}")
        else:
            print("You can not carry more than 4 potions. Leaving this one "
                  "behind")
    elif roll == 3:
        ring = adventurer.magic_ring
        if not ring:
            print("You have found a Ring of Trap Detection! You now can avoid "
                  "traps.")
            ring = True
        else:
            print("You already have a Ring of Trap Detection. Leaving this one"
                  "behind")
    elif roll == 4:
        magic_armour = adventurer.magic_armour
        if not magic_armour:
            print("You have found a Magic Armour! Your Armour Class now is 9.")
            magic_armour = "Magic Armour"
            adventurer.armour_class = 9
        else:
            print("You already have a Magic Armour. Leaving this one behind.")
    elif roll == 5:
        coins = adventurer.gold_coins
        coin_roll = Dice.roll(1) * 1000
        print(f"You found {coin_roll} Gold Coins!")
        if coins > 14000:
            print("You can not carry more than 14.000 Gold Coins. Leaving "
                  "these behind.")
        elif coins + coin_roll >= 14000:
            print("You can not carry more than 14.000 coins. You grab what "
                  "you can and leave the rest behind. You now have 14000 "
                  "Gold Coins")
        else:
            coins += coin_roll
            print(f"You grab the Gold Coins. You now have {coins} Gold Coins.")
    elif roll == 6:
        damage = Dice.roll(1)
        print(f"You have found a Cursed Item! You take {damage} damage.")
        hp = adventurer.current_health_points
        hp -= damage
        if hp <= 0:
            print("You died.")
            adventurer.is_alive = False
        else:
            print(f"You have {hp} Health Points left.")

