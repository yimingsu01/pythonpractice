from gameoflife.LifeGrid import LifeGrid
from os import system
import time
import random

# INIT_CONFIG = [[10, 10], [10, 8], [9, 9], [11, 9], [12, 9], [8, 9], [7, 9], [13, 9]]
INIT_CONFIG = [[10, 10], [10, 8], [9, 9], [11, 9], [12, 9], [8, 9]]
# for i in range(0, 9, 1):
#     temp = []
#     temp.append(random.randint(0, 9))
#     temp.append(random.randint(0, 9))
#     INIT_CONFIG.append(temp.copy())
# print(INIT_CONFIG)



GRID_WIDTH = 20
GRID_HEIGHT = 20

NUM_GENS = 100

def main():
    grid = LifeGrid(GRID_HEIGHT, GRID_WIDTH)
    grid.configure(INIT_CONFIG)

    draw(grid.grid)
    for i in range(NUM_GENS):
        time.sleep(0.5)
        evolve(grid)
        draw(grid.grid)

def evolve(grid):
    liveCells = list()
    for i in range(grid.numRows()):
        for j in range(grid.numCols()):
            neighbors = grid.numLiveNeighbors(i, j)
            if (neighbors == 2 and grid.isLiveCell(i, j)) or (neighbors == 3):
                liveCells.append([i, j])
    grid.configure(liveCells)

def draw(grid):
    _ = system("cls")
    for i in grid:
        print(i)


if __name__ == '__main__':
    main()