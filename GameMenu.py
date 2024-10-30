from logging import addLevelName

import Movement
from Adventurer import Adventurer

def game_menu():
    turn = 1
    running = True
    adventurer = Adventurer()

    while running:

        if turn <= 30:
            print(f"Turn: {turn}\n")
            op = input("Chose an option:\n"
                       "\n"
                       "1 - Movement\n"
                       "\n"
                       "2 - Use potion\n"
                       "\n"
                       "3 - See stats and items\n"
                       "\n"
                       "0 - Quit game\n")

            if op == "1":
                Movement.normal_movement(adventurer)
                turn += 1
            elif op == "2":
                adventurer.drink_potion()
            elif op == "3":
                adventurer.show_stats()
            elif op == "0":
                running = False
            else:
                print("Invalid option.")

            if not adventurer.is_alive:
                running = False

        else:
            print("end")