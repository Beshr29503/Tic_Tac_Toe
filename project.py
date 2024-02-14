"""
Tic_Tac_Toe
Ibrahim Mohamed Nabil Mohamed Beshr
Github Username: Beshr29503
edx    Username: i-beshr
Alexandria, Egypt
14-02-2024
"""
from game import Game


def main():
    greet_game()
    mode = select_mode()
    start_game(mode)


def greet_game():
    print("Welcome to Tic_Tac_Toe Game!")
    return True


def select_mode():
    mode = 0
    print("-------------------------")
    print("Choose Mode:\n1.One Player Mode\n2.Two Player Mode")
    while mode != '1' and mode != '2':
        mode = input("Please Insert 1 or 2:")
    return mode


def start_game(mode):
    Game(mode)


if __name__ == "__main__":
    main()