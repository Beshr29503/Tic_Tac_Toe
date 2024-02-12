from modes import One_player,Two_player
import grid


class Game():
    def __init__(self):
        self.end_game = False
        self.mode = 0
        self.player = None

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


    @property
    def end_game(self):
        return self._end_game
    

    @end_game.setter
    def end_game(self,status):
        self._end_game = status


    def play(self):
        while self.end_game == False:
            if self.mode == 1:
                cell = 0
                print("-------------------------")
                while cell < 1 or cell > 9:
                    try:
                        cell = int(input("Please Insert A Number 1 to 9 According to Grid:"))
                    except ValueError:
                        cell = 0

            elif self.mode == 2:
                pass

            self._end_game = True
