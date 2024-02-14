from player import Human_player,Computer_player
from grid import Grid
import random
import csv
import sys



class Game():
    def __init__(self,mode):
        self.mode    = mode
        self._circle = 'O'
        self._cross  = 'X'
        self.player_one = None
        self.player_two = None
        self.ground = Grid()

        self.grid = None
        self.valid = [1,2,3,4,5,6,7,8,9]

        self.startup()


    @property
    def circle(self):
        return self._circle
    

    @property
    def cross(self):
        return self._cross


    @property
    def ground(self):
        return self._ground
   
    
    @ground.setter
    def ground(self,g):
        self._ground = g

    
    def startup(self):
        icon = ''
        
        if self.mode == '1':
            self.player_one = Human_player('1')
            self.player_two = Computer_player()
            print("-------------------------")
            print("Choose Icon:\n1." + self.circle + "\n2." + self.cross)
            while icon != '1' and icon != '2':
                icon = input("Please Insert 1 or 2:")
        elif self.mode == '2':
            self.player_one = Human_player('1')
            self.player_two = Human_player('2')
            print("-------------------------")
            print("Player 1")
            print("Choose Icon:\n1." + self.circle + "\n2." + self.cross)
            while icon != '1' and icon != '2':
                icon = input("Please Insert 1 or 2:")

        if icon == '1':
            self.player_one._icon = self.circle
            self.player_two._icon = self.cross
        elif icon == '2':
            self.player_one._icon = self.cross
            self.player_two._icon = self.circle

        self.ground.draw_grid()
        self.play()


    def play(self):
        while True:
            if self.mode == '1':
                self.player_move(self.player_one)
                self.computer_move(self.player_two)
                
            elif self.mode == '2':
                self.player_move(self.player_one)
                self.player_move(self.player_two)
    
    
    def player_move(self,player):
        if len(self.valid) == 0:
            sys.exit("Draw!!!")
        else:
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


    def computer_move(self,player):
        if len(self.valid) == 0:
            sys.exit("Draw!!!")
        else:
            print("-------------------------")
            print("Computer Turn!!!")
            cell = random.choice(self.valid)
            self.edit_csv(cell,player)
            self.ground.draw_grid()
            self.win_state(player)
            self.valid.remove(cell)


    def edit_csv(self,cell,player):
        with open('squares.csv', 'r') as file:
            self.grid  = []
            for line in file:
                left_column, middle_column, right_column = line.strip().split(",")
                if left_column == self._circle or left_column == self._cross:
                    pass
                elif int(left_column) == cell:
                    left_column = player._icon
                if middle_column == self._circle or middle_column == self._cross:
                    pass
                elif int(middle_column) == cell:
                    middle_column = player._icon
                if right_column == self._circle or right_column == self._cross:
                    pass
                elif int(right_column) == cell:
                    right_column = player._icon
                c = {"Left":left_column,"Middle":middle_column,"Right":right_column}
                self.grid.append(c)
        with open('squares.csv','w') as file:
            writer = csv.DictWriter(file, fieldnames=['Left','Middle','Right'])
            writer.writerows(self.grid)


    def win_state(self,player):
       if (
        (self.grid[0]['Left'] == player._icon and self.grid[0]['Middle'] == player._icon and self.grid[0]['Right'] == player._icon) or 
        (self.grid[1]['Left'] == player._icon and self.grid[1]['Middle'] == player._icon and self.grid[1]['Right'] == player._icon) or 
        (self.grid[2]['Left'] == player._icon and self.grid[2]['Middle'] == player._icon and self.grid[2]['Right'] == player._icon) or
        (self.grid[0]['Left'] == player._icon and self.grid[1]['Left'] == player._icon and self.grid[2]['Left'] == player._icon) or
        (self.grid[0]['Middle'] == player._icon and self.grid[1]['Middle'] == player._icon and self.grid[2]['Middle'] == player._icon) or
        (self.grid[0]['Right'] == player._icon and self.grid[1]['Right'] == player._icon and self.grid[2]['Right'] == player._icon) or 
        (self.grid[0]['Left'] == player._icon and self.grid[1]['Middle'] == player._icon and self.grid[2]['Right'] == player._icon) or 
        (self.grid[2]['Left'] == player._icon and self.grid[1]['Middle'] == player._icon and self.grid[0]['Right'] == player._icon)
       ):
        print(player,"Won!!!")
        sys.exit("Game Ended!!!")
       else:
           return