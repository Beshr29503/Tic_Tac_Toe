from emoji import emojize
from grid import Grid


class One_player():
    def __init__(self):
        self._circle = emojize(":hollow_red_circle:")
        self._cross  = emojize(":cross_mark:")
        self._ground = None
        self._icon = 0

        self.startup()
        

    def startup(self):
        print("-------------------------")
        print("Choose Icon:\n1." + self.circle + "\n2." + self.cross)
        while self.icon != 1 and self.icon != 2:
            try:
                self.icon = int(input("Please Insert 1 or 2:"))
            except ValueError:
                self.icon = 0

        if self.icon == 1:
            print("-------------------------")
            print("Game Started!\nYou are " + self.circle)
            self.icon = self.circle
            self.ground = Grid()
            self.ground.draw_grid()
        elif self.icon == 2:
            print("-------------------------")
            print("Game Started!\nYou are " + self.cross)
            self.icon = self.cross
            self.ground = Grid()
            self.ground.draw_grid()


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
    

    @property
    def icon(self):
        return self._icon
    

    @icon.setter
    def icon(self,i):
        self._icon = i




class Two_player():
    def __init__(self):
        pass