# Tic_Tac_Toe
### Video Demo : <URL>
# Description
This repository implements the backend of a Tic_Tac_Toe game including the following features:
* One Player Mode
* Two Player Mode
* Ability to choose icon ( X or O )
## ***project.py***
This python file project.py startup the Tic_Tac_Toe game by executing the following functions:
* **greet_game**

This function greets the user/s by printing to the screen "Welcome to Tic_Tac_Toe Game!!!"
* **select_mode**

This function prompts the user/s to enter '1' for (One Player Mode) and '2' for (Two Player Mode) accepting only these two values and rejecting any other unaccepted value through validation using the following while loop and returning the value of the user input:

	while mode != '1' and mode != '2':
        mode = input("Please Insert 1 or 2:")
    return mode

* **start_game**

This function creates an object of class Game that will be discussed later passing the user input mode as a parameter in order to start playing.

## ***game.py***
This python file game.py implements the class Game that contains the whole logic of the game. Game contains many attributes and methods which are:

### Attributes

1. **player_one** : object of class Player (must be Human)
2. **player_two** : object of class Player (Human/Computer)
3. **mode** : represent mode chosen by user
4. **circle** : represent the entity 'O' of game
5. **cross** : represent the entity 'X' of game
6. **valid** : list to represent valid squares in the grid
7. **ground**: object of class grid that represent the playground of the game

### Methods

* **startup**

This method prompts the user/s to enter '1' (O) or '2' (X) to decide which icon to play with throughout the game. Moreover, it creates the object "player_one" and object "player_two" then draws the grid (playground) to show the user all the valid squares.

* **play**

This method holds the role of calling both methods
1. **player_move**
2. **computer_move**

according to the mode addressed by the user.

* **player_move**

This method prompts the user to input a valid square (1-9) from the grid (playground) in order to apply his move then edit the csv file "squares.csv" that represents the data in the grid by reading and writing to the file. Also, it pops up to the user the updated grid after the move is done and checks if there is a winning streak in order to end the game or not. That is all demonstrated in the following code snippet:

    cell = 0
    print("-------------------------")
    while self.valid.__contains__(cell) == False:
        try:
            print(player,"Turn!!!")
            cell = int(input("Please Insert A Number 1 to 9 According to Grid:"))
        except ValueError:
            cell = 0
        self.edit_csv(cell,player)
        self.ground.draw_grid()
        self.win_state(player)
        self.valid.remove(cell)

* **computer_move**

This method implements the same logic as "player_move" method but using the 'Random' module to decide which square in the grid the computer will insert his icon in. That is all demonstrated in the following code snippet:

    print("-------------------------")
    print("Computer Turn!!!")
    cell = random.choice(self.valid)
    self.edit_csv(cell,player)
    self.ground.draw_grid()
    self.win_state(player)
    self.valid.remove(cell)

* **win_state**

This method implements the algorithm to check after each move whether there is a winning streak and game should end by 'sys.exit()' or not.

## ***player.py***

This python file implements three classes:

* Parent Class: Player
* Child 1 Class: Human_player
* Child 2 Class: Computer_player 

Each class has an instance variable ( attribute ) 'icon' that represents the entity that the player can play with (O) or (X).

## ***grid.py***

This python file implements class Grid that only has two methods which are:
* startup: this method draws the initial grid even before the very first move
* draw_grid: this method draws the grid after each individual move showing the updated grid to the user

## ***test_projects.py***

This python file implements test cases to the three functions in ***project.py*** other than the main function.