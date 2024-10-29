from Adventurer import Adventurer


def game_menu():
    turn = 1
    running = True
    adventurer = Adventurer()

    while adventurer.is_alive:
        if turn <= 30:
            print(f"Turn: {turn}")
            op = input()
        else:
            pass