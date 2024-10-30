from GameMenu import game_menu

def main_menu():

    running = True
    while running:

        op = input("Welcome to the Berdolock's Fortress\n"
              "\n"
              "Chose an option:\n"
              "\n"
              "1 - play\n"
              "0 - quit\n")

        if op == "1":
            game_menu()
        elif op == "0":
            running = False
        else:
            print("Invalid option.")