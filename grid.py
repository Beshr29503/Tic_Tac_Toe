from tabulate import tabulate


class Grid():
    def __init__(self):
        self._grid = []


    def draw_grid(self):
        with open('squares.csv', 'r') as file:
            for line in file:
                left_column, middle_column, right_column = line.strip().split(",")
                c = {"Left":left_column,"Middle":middle_column,"Right":right_column}
                self.grid.append(c)
            print(tabulate(self.grid, tablefmt = "simple_grid"))


    @property
    def grid(self):
        return self._grid