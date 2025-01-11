import sys
"""
    File: battleship.py
    Author: Samyak Gurung
    Course: CSC 120, Spring 2024
    Purpose: this code creates a 2d game
    battleship which uses classes as objects and the 
    playing feild where the player or puts a file for 
    the ships and guess which is then filtered out
    on whether the player had put correct guess, 
    locations, etc.
"""
class GridPos:
    """
    The class represents an object holding the positions in
    the grid table below 
    
    Where the object contains instances storing the x and y
    coordinate, whether there is a ship or not and whether
    the ship has been hit or not
    """
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._double = 0
        self._ship = None
        self._hitcount = 0
    
    def x(self):
        return self._x

    def y(self):
        return self._y

    def check_node(self):
        if self._ship == None:
            return

    def hit_check(self, board):
        """
        The function checks whether the node
        hits a ship and whether the node sinks
        the ship
        parameter: the class object and the board
        class
        return: None
        """
        if self._ship != None:
            if self._hitcount <= 0:
                board._ships[self._ship._type] -= 1
                if board._ships[self._ship._type] <= 0:
                    print(f'{self._ship._type}'+' sunk')
                    self._hitcount += 1
                    board._ship_count -= 1
                else:
                    print('hit')
                    self._hitcount += 1
            elif self._hitcount > 0:
                print('hit (again)')
        elif self._ship == None:
            if self._hitcount == 0:
                self._hitcount += 1
                print('miss')
            elif self._hitcount > 0:
                print('miss (again)')
        return

    def __str__(self):
        return f'({self._x}, {self._y})'

class Board:
    """
    This class represents the main board for 
    the game it stores all the objects that the
    file give
    
    It is a 10x10 grid created by double linked list
    which stores the gridpos class as its nodes
    and uses ships to distinguish elements
    """
    def __init__(self):
        self._grid = []
        for i in range(10):
            new = []
            for j in range(10):
                new.append(GridPos(i, j))
            self._grid.append(new)
        self._ships = {'A': 5, 'B': 4, 'S': 3, 'D': 3, 'P': 2}
        self._ship_count = 5

    def guess_checker(self, val):
        return

    def place_one_ship(self, list_):
        """
        places a ship and uses methods in the
        class to store the ships at locations
        """
        type_ = list_[0]
        num1 = 0
        num2 = 0
        
        if list_[1] == list_[3]:
            num1 = int(max(int(list_[2]), int(list_[4])))
            num2 = int(min(int(list_[2]), int(list_[4])))
        elif list_[2] == list_[4]:
            num1 = int(max(int(list_[1]), int(list_[3])))
            num2 = int(min(int(list_[1]), int(list_[3])))
        size = num1 - num2 + 1
        # the for loop iterates through the board and adds ships
        for i in range(size):
            cur_x = 0
            cur_y = 0
            check = False
            ship = None
            if list_[1] == list_[3]:
                cor_x = int(list_[1])
                cor_y = min(int(list_[2]), int(list_[4])) + i
                ship = Ship(type_, size, [cor_x, cor_y], int(size))
                check = True
            elif list_[2] == list_[4]:
                cor_y = int(list_[2])
                cor_x = min(int(list_[1]), int(list_[3])) + i
                ship = Ship(type_, size, [cor_x, cor_y], int(size))
                check = True
            
            if check == False:
                string = "ERROR: ship not horizontal or vertical:"
                print(string + ''.join(list_))
                sys.exit(0)
            if size_checker(list_[0], size)!= True:
                print("ERROR: incorrect ship size: " + ' '.join(list_))
                sys.exit(0)
            if cor_x > 9 or cor_y > 9:
                print("ERROR: ship out-of-bounds: " + ''.join(list_))
                sys.exit(0)
            elif self._grid[cor_y][cor_x]._ship != None:
                print("ERROR: overlapping ship: " + ''.join(list_))
                sys.exit(0)
            self._grid[cor_y][cor_x]._ship = ship

    def __str__(self):
        for i in range(1, len(self._grid)+1):
            print(self._grid[-i])
        return ''

class Ship:
    """
    this class  stores the ships and all values related to
    the specified ship
    it takes in 4 arguments and stores it for later use 
    in the playing of the game it is stored in the grid position
    the data is used later in the code to check life points and
    current state of the ship
    """
    def __init__(self, type_, size, pos, life):
        self._type = type_
        self._size = size
        self._gridpos = None
        self._pts = int(life)

    def __str__(self):
        tp = self._type
        sz = self._size
        gp = self._gridpos
        pt = self._pts
        return f'{tp}, {sz}, {gp}, {pt}'

def size_checker(type_, size):
    """
    a function that generates the text using a hash table
    similar to the writer bot and stores it in a list
    adjusted for hash table
    parameter: a list and two integer
    return a list
    """
    ship_size = [['A', 5],['B', 4],['S',3],['D',3],['P',2]]
    if type_ == 'A':
        if size != ship_size[0][1]:
            return False
    if type_ == 'B':
        if size != ship_size[1][1]:
            return False
    if type_ == 'S':
        if size != ship_size[2][1]:
            return False
    if type_ == 'D':
        if size != ship_size[3][1]:
            return False
    if type_ == 'P':
        if size != ship_size[4][1]:
            return False
    return True

def checker_(file, board):
    """
    a function that checks whether the users guess is
    correct or not through iterating the file and checking
    the grid position
    parameter: a class that stores the board
    return: None
    """
    ships = 5
    ships_cor = {'A': 5, 'B': 4, 'S':3, 'D': 3, 'P': 2}
    for line in file:
        line = line.strip().split()
        y_val = int(line[1])
        x_val = int(line[0])
        if x_val > 9 or y_val > 9:
            print("illegal guess")
            continue
        cord = board._grid[y_val][x_val]
        if cord._ship != None:
            cord.hit_check(board)
        elif cord._ship == None:
            cord.hit_check(board)
        if board._ship_count == 0:
            print("all ships sunk: game over")
            sys.exit(0)

def main():
    file = open(input())
    board = Board()
    ships = []
    comp = 0
    for line in file:
        line = line.split()
        ships.append(line[0])
        board.place_one_ship(line)
        comp += 1
    if comp > 5 or comp < 5:
        print("ERROR: fleet composition incorrect")
        sys.exit(0)
    for i in range(len(ships)):
        for j in range(len(ships)):
            if ships[i] == ships[j] and i != j:
                print("ERROR: fleet composition incorrect")
                sys.exit(0)
    g_file = open(input())
    checker = checker_(g_file, board)
    checker
    file.close()
    g_file.close()
main()
    