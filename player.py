class Player():
    def __init__(self,n):
        self._icon = 0
        self._name = n

    @property
    def icon(self):
        return self._icon
    

    @icon.setter
    def icon(self,i):
        self._icon = i


    @property
    def name(self):
        return self._name
    

    @name.setter
    def name(self,n):
        self._name = n


class Human_player(Player):
    def __init__(self,n):
        super().__init__(n)

    def __str__(self):
        return 'Player ' + self._name


class Computer_player(Player):
    def __init__(self):
        pass

    def __str__(self):
        return 'Computer'