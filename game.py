from modes import One_player,Two_player
from grid import Grid
import random
import csv
import sys



class Game():
    def __init__(self):
        self.mode   = 0
        self.player = None
        self.ground = Grid()

        self.grid = None
        self.valid = [1,2,3,4,5,6,7,8,9]

        self.startup()
        self.play()


    def startup(self):
        print("Choose Mode:\n1.One Player Mode\n2.Two Player Mode")
        
        while self.mode != 1 and self.mode != 2:
            try:
                self.mode = int(input("Please Insert 1 or 2:"))
            except ValueError:
                self.mode = 0
        
        if self.mode == 1:
            self.player = One_player()
        elif self.mode == 2:
            self.player = Two_player()

        self.ground.draw_grid()


    @property
    def ground(self):
        return self._ground
   
    
    @ground.setter
    def ground(self,g):
        self._ground = g


    def play(self):
        while True:
            if self.mode == 1:
                self.player_move()
                self.comp_move()
                
            elif self.mode == 2:
                pass


    def player_move(self):
        cell = 0
        print("-------------------------")
        while self.valid.__contains__(cell) == False:
            try:
                print("Your Turn!!!")
                cell = int(input("Please Insert A Number 1 to 9 According to Grid:"))
            except ValueError:
                cell = 0
        self.edit_csv(cell,1)
        self.ground.draw_grid()
        self.win_state()
        if len(self.valid) == 0:
            sys.exit("Draw!!!")
        else:
            self.valid.remove(cell)


    def comp_move(self):
        if len(self.valid) == 0:
            sys.exit("Draw!!!")
        else:
            print("-------------------------")
            print("Computer Turn!!!")
            cell = random.choice(self.valid)
            self.edit_csv(cell,2)
            self.ground.draw_grid()
            self.win_state()
            self.valid.remove(cell)


    def edit_csv(self,cell,control):
        with open('squares.csv', 'r') as file:
            self.grid  = []
            for line in file:
                left_column, middle_column, right_column = line.strip().split(",")
                if left_column == self.player._circle or left_column == self.player._cross:
                    pass
                elif int(left_column) == cell and control == 1:
                    left_column = self.player._icon
                elif int(left_column) == cell and control == 2:
                    left_column = self.player._comp
                if middle_column == self.player._circle or middle_column == self.player._cross:
                    pass
                elif int(middle_column) == cell and control == 1:
                    middle_column = self.player._icon
                elif int(middle_column) == cell and control == 2:
                    middle_column = self.player._comp
                if right_column == self.player._circle or right_column == self.player._cross:
                    pass
                elif int(right_column) == cell and control == 1:
                    right_column = self.player._icon
                elif int(right_column) == cell and control == 2:
                    right_column = self.player._comp 
                c = {"Left":left_column,"Middle":middle_column,"Right":right_column}
                self.grid.append(c)
        with open('squares.csv','w') as file:
            writer = csv.DictWriter(file, fieldnames=['Left','Middle','Right'])
            writer.writerows(self.grid)


    def win_state(self):
       if self.grid[0]['Left'] == self.player._icon and self.grid[0]['Middle'] == self.player._icon and self.grid[0]['Right'] == self.player._icon:
           sys.exit("You Won!!!")
       elif self.grid[0]['Left'] == self.player._comp and self.grid[0]['Middle'] == self.player._comp and self.grid[0]['Right'] == self.player._comp:
           sys.exit("Computer Won!!!")
       if self.grid[1]['Left'] == self.player._icon and self.grid[1]['Middle'] == self.player._icon and self.grid[1]['Right'] == self.player._icon:
           sys.exit("You Won!!!")
       elif self.grid[1]['Left'] == self.player._comp and self.grid[1]['Middle'] == self.player._comp and self.grid[1]['Right'] == self.player._comp:
           sys.exit("Computer Won!!!")
       if self.grid[2]['Left'] == self.player._icon and self.grid[2]['Middle'] == self.player._icon and self.grid[2]['Right'] == self.player._icon:
           sys.exit("You Won!!!")
       elif self.grid[2]['Left'] == self.player._comp and self.grid[2]['Middle'] == self.player._comp and self.grid[2]['Right'] == self.player._comp:
           sys.exit("Computer Won!!!")
       if self.grid[0]['Left'] == self.player._icon and self.grid[1]['Left'] == self.player._icon and self.grid[2]['Left'] == self.player._icon:
           sys.exit("You Won!!!")
       elif self.grid[0]['Left'] == self.player._comp and self.grid[1]['Left'] == self.player._comp and self.grid[2]['Left'] == self.player._comp:
           sys.exit("Computer Won!!!")
       if self.grid[0]['Middle'] == self.player._icon and self.grid[1]['Middle'] == self.player._icon and self.grid[2]['Middle'] == self.player._icon:
           sys.exit("You Won!!!")
       elif self.grid[0]['Middle'] == self.player._comp and self.grid[1]['Middle'] == self.player._comp and self.grid[2]['Middle'] == self.player._comp:
           sys.exit("Computer Won!!!")
       if self.grid[0]['Right'] == self.player._icon and self.grid[1]['Right'] == self.player._icon and self.grid[2]['Right'] == self.player._icon:
           sys.exit("You Won!!!")
       elif self.grid[0]['Right'] == self.player._comp and self.grid[1]['Right'] == self.player._comp and self.grid[2]['Right'] == self.player._comp:
           sys.exit("Computer Won!!!")
       if self.grid[0]['Left'] == self.player._icon and self.grid[1]['Middle'] == self.player._icon and self.grid[2]['Right'] == self.player._icon:
           sys.exit("You Won!!!")
       elif self.grid[0]['Left'] == self.player._comp and self.grid[1]['Middle'] == self.player._comp and self.grid[2]['Right'] == self.player._comp:
           sys.exit("Computer Won!!!")
       if self.grid[2]['Left'] == self.player._icon and self.grid[1]['Middle'] == self.player._icon and self.grid[0]['Right'] == self.player._icon:
           sys.exit("You Won!!!")
       elif self.grid[2]['Left'] == self.player._comp and self.grid[1]['Middle'] == self.player._comp and self.grid[0]['Right'] == self.player._comp:
           sys.exit("Computer Won!!!")
       else:
           return