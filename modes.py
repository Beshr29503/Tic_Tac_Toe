from emoji import emojize


class One_player():
    def __init__(self):
        self._circle = emojize(":hollow_red_circle:")
        self._cross  = emojize(":cross_mark:")
        self._icon = 0
        self._comp = None

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
            self.comp = self.cross
        elif self.icon == 2:
            print("-------------------------")
            print("Game Started!\nYou are " + self.cross)
            self.icon = self.cross
            self.comp = self.circle


    @property
    def circle(self):
        return self._circle
    

    @property
    def cross(self):
        return self._cross
    

    @property
    def icon(self):
        return self._icon
    

    @icon.setter
    def icon(self,i):
        self._icon = i


    @property
    def comp(self):
        return self._comp
    

    @comp.setter
    def comp(self,c):
        self._comp = c




class Two_player():
    def __init__(self):
        pass