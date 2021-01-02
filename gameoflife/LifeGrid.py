class LifeGrid():
    grid = []
    nrows = 0
    ncols = 0

    def __init__(self, nrows, ncols):
        temp = []
        self.nrows = nrows
        self.ncols = ncols
        for i in range(0, ncols, 1):
            temp.append(0)
        for i in range(0, nrows, 1):
            self.grid.append(temp.copy())

    def numRows(self):
        return self.nrows

    def numCols(self):
        return self.ncols

    def configure(self, coordList):
        i = 0
        j = 0
        while i < self.nrows:
            j = 0
            while j < self.ncols:
                if [i, j] in coordList:
                    self.setCell(i, j)
                else:
                    self.clearCell(i, j)
                j += 1
            i += 1
        for i in self.grid:
            print(i)

    def clearCell(self, row, col):
        self.grid[row][col] = "__"

    def setCell(self, row, col):
        self.grid[row][col] = "@@"

    def isLiveCell(self, row, col):
        # print(self.grid[row][col])
        if self.grid[row][col] == "@@":
            return True
        else:
            return False

    def numLiveNeighbors(self, row, col):
        alive = 0
        try:
            if self.isLiveCell(row - 1, col - 1) and (row - 1 >= 0 and col - 1 >= 0):
                alive += 1
            if self.isLiveCell(row - 1, col) and (row - 1 >= 0):
                alive += 1
            if self.isLiveCell(row - 1, col + 1) and (row - 1 >= 0 and col + 1 < self.ncols):
                alive += 1
            if self.isLiveCell(row, col - 1) and (col - 1 >= 0):
                alive += 1
            if self.isLiveCell(row, col + 1) and (col + 1 < self.ncols):
                alive += 1
            if self.isLiveCell(row + 1, col - 1) and (row + 1 < self.nrows and col - 1 >= 0):
                alive += 1
            if self.isLiveCell(row + 1, col) and (row + 1 < self.nrows):
                alive += 1
            if self.isLiveCell(row + 1, col + 1) and (row + 1 < self.nrows and col + 1 < self.ncols):
                alive += 1
        except IndexError:
            pass
        return alive

