"""
    File: word_grid.py
    Author: Samak Gurung
    Course: CSC 120, Fall 2024
    Purpose: This program processes two inputs grid size and seed value that is 
    used to map the grid size and the seed for the random input. The code then
    uses for loops to repeatedly add random letters in a list of list which is then
    printed.
"""
import random
def init():
    """
    gets the grid size and random seed value
    Parameters: grid_size and seed value store integers
    Returns: a number that is used as the grid size and the seed value for the grid
    """
    grid_size = int(input())
    seed_value = input()
    random.seed(seed_value)
    grid = make_grid(grid_size)
    return print_grid(grid)

def make_grid(grid_size):
    """
    stores the random letters in the grid
    Parameters: grid that stores the list of lists as a grid and the letters
    Returns: a list of lists
    """
    grid = []
    num = grid_size*grid_size
    for i in range(grid_size):
        grid.append([])
        for j in range(grid_size):
            letter = chr(random.randint(97, 122))
            grid[i].append(letter)
    return grid
def print_grid(grid):
    """
    prints the grid
    """
    for i in grid:
        print(','.join(i))

def main():
    grid_size = init(g)
    grid = make_grid(grid_size)
    print_grid(grid)
if __name__ == "__main_":
    main()
init()
