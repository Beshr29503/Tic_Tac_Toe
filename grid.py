from tabulate import tabulate
import csv


class Grid():
    def __init__(self):
        self._grid = None
        self.startup()


    def startup(self):
        squares = [{'Left':1,'Middle':2,'Right':3},
                   {'Left':4,'Middle':5,'Right':6},
                   {'Left':7,'Middle':8,'Right':9}
                   ]
        with open('squares.csv', 'w') as file:
            writer = csv.DictWriter(file, fieldnames=['Left','Middle','Right'])
            writer.writerows(squares)


    def draw_grid(self):
        self._grid = []
        with open('squares.csv', 'r') as file:
            for line in file:
                left_column, middle_column, right_column = line.strip().split(",")
                c = {"Left":left_column,"Middle":middle_column,"Right":right_column}
                self.grid.append(c)  
            print(tabulate(self.grid, tablefmt = "simple_grid"))


    @property
    def grid(self):
        return self._grid