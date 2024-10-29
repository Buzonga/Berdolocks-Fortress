def main_menu():

    running = True
    while running:

        op = input("Welcome to the Berdolock's Fortress\n"
              "\n"
              "Chose an option:\n"
              "\n"
              "1 - play\n"
              "0 - quit")
        if op == 1:
            pass
        elif op == 0:
            running = False
        else:
            print("Invalid option.")