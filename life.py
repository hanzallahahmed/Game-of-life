from array2 import Array2D


class Life_Grid:
    DEAD_CELL = '.'
    LIVE_CELL = '@'

    def __init__(self, numRows, numCols):
        self.rows = numRows
        self.cols = numCols
        self._grid = Array2D(numRows, numCols)
        self.configure(list())

    def numRows(self):
        return self._grid.numRows()

    def numCols(self):
        return self._grid.numCols()

    def __getitem__(self, ndxTuple):
        return self._grid[ndxTuple[0], ndxTuple[1]]

    def configure(self, coordList):
        for i in range(self.rows):
            for j in range(self.cols):
                self.clearCell(i, j)
        for coord in coordList:
            self.setCell(coord[0], coord[1])

    def isLiveCell(self, row, col):
        return self._grid[row, col] == Life_Grid.LIVE_CELL

    def isDead(self, row, col):  # CHECKS FOR THE DEAD CELL
        if self._grid[row, col] == Life_Grid.DEAD_CELL:
            return True
        else:
            return False

    def alive(self, ndxtuple):
        self._grid[ndxtuple[0], ndxtuple[1]] = Life_Grid.LIVE_CELL

    def clearCell(self, row, col):
        self._grid[row, col] = Life_Grid.DEAD_CELL

    def setCell(self, row, col):
        self._grid[row, col] = Life_Grid.LIVE_CELL

    def numLiveNeighbors(self, row, col):
        tmp = 0
        row_above = row - 1 if row > 0 else row
        left_col = col - 1 if col > 0 else col
        right_col = col + \
            1 if col < (self.numCols() - 1) else self.numCols()-1
        row_below = row + \
            1 if row < (self.numRows() - 1) else self.numRows() - 1

        for i in range(row_above, row_below + 1):
            for j in range(left_col, right_col + 1):
                if (i == row and j == col):
                    continue
                if self.isLiveCell(i, j):
                    tmp += 1
        return tmp

    def __iter__(self):
        return self

    def draw(_grid):
        for i in range(_grid.numRows()):
            print('')
            for j in range(_grid.numCols()):
                print(_grid[i, j], end=' ')


INIT_CONFIG = [(1, 2), (2, 1), (2, 2), (2, 3)]

GRID_WIDTH = int(input("Enter the grid width: "))

GRID_HEIGHT = int(input("Enter the grid height: "))

NUM_GENS = int(input("Enter the num of generation to prompt: "))
grid = Life_Grid(GRID_WIDTH, GRID_HEIGHT)


def gameOfLife():
    grid = Life_Grid(GRID_WIDTH, GRID_HEIGHT)
    grid.configure(INIT_CONFIG)

    draw(grid)
    for _ in range(NUM_GENS):
        evolve(grid)
        draw(grid)


def evolve(grid):
    livecells = []
    for row in range(grid.rows):
        for col in range(grid.cols):
            neighbors = grid.numLiveNeighbors(row, col)

            if (neighbors == 2 and grid.isLiveCell(row, col)) or neighbors == 3:
                livecells.append((row, col))
    grid.configure(livecells)
    print(" ")


def draw(grid):
    for i in range(grid.numRows()):
        print('')
        for j in range(grid.numCols()):
            print(grid[i, j], end=' ')


gameOfLife()
