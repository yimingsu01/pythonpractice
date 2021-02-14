class Maze():
    maze = []
    numRows = 0
    numCols = 0
    walls = []
    start = 0
    end = 0
    path = []

    def __init__(self, numRows, numCols):
        self.numCols = numCols
        self.numRows = numRows
        i = 0
        while i < numRows:
            temp_list = []
            j = 0
            while j < numCols:
                temp_list.append("  ")
                j += 1
            self.maze.append(temp_list.copy())
            i += 1

    def setWall(self, row, col):
        if (max(0, row) == row and max(row, self.numRows) == self.numRows) and (
                max(0, col) == col and max(col, self.numCols) == self.numCols):
            self.maze[row][col] = "@@"
            self.walls.append([row, col])
        else:
            return -1

    def setStart(self, row, col):
        if (max(0, row) == row and max(row, self.numRows) == self.numRows) and (
                max(0, col) == col and max(col, self.numCols) == self.numCols):
            self.maze[row][col] = "SS"
            self.start = [row, col]
        else:
            return -1

    def setExit(self, row, col):
        if (max(0, row) == row and max(row, self.numRows) == self.numRows) and (
                max(0, col) == col and max(col, self.numCols) == self.numCols):
            self.maze[row][col] = "EE"
            self.end = [row, col]
        else:
            return -1

    def draw(self):
        for i in self.maze:
            print(i)

    def testExit(self):
        try:
            if self.maze[self.end[0] - 1][self.end[1]] == "@@" \
                    and self.maze[self.end[0] + 1][self.end[1]] == "@@" \
                    and self.maze[self.end[0]][self.end[1] - 1] == "@@" \
                    and self.maze[self.end[0] - 1][self.end[1] + 1] == "@@":
                return False
            else:
                return True
        except IndexError:
            pass

    def findPath(self, curr_pos):
        if not self.testExit():
            print("Exit blocked!")
            return -1

        up = [curr_pos[0] - 1, curr_pos[1]]
        if up[0] < 0:
            up = self.walls[0]

        down = [curr_pos[0] + 1, curr_pos[1]]
        if down[0] >= self.numRows:
            down = self.walls[0]

        left = [curr_pos[0], curr_pos[1] - 1]
        if left[1] < 0:
            left = self.walls[0]

        right = [curr_pos[0], curr_pos[1] + 1]
        if right[1] >= self.numCols:
            right = self.walls[0]
        block = True

        if up == self.end or down == self.end or right == self.end or left == self.end:
            self.maze[curr_pos[0]][curr_pos[1]] = "OO"
            return 1

        try:
            if not (up in self.walls):
                if not up in self.path:
                    self.maze[curr_pos[0]][curr_pos[1]] = "OO"
                    self.path.append(up)
                    self.findPath(up)
                    block = False
            # else:
            #     self.maze[curr_pos[0]][curr_pos[1]] = "XX"

            if not (right in self.walls):
                if not right in self.path:
                    self.maze[curr_pos[0]][curr_pos[1]] = "OO"
                    self.path.append(right)
                    self.findPath(right)
                    block = False
            # else:
            #     self.maze[curr_pos[0]][curr_pos[1]] = "XX"

            if not (down in self.walls):
                if not down in self.path:
                    self.maze[curr_pos[0]][curr_pos[1]] = "OO"
                    self.path.append(down)
                    self.findPath(down)
                    block = False
            # else:
            #     self.maze[curr_pos[0]][curr_pos[1]] = "XX"

            if not (left in self.walls):
                if not left in self.path:
                    self.maze[curr_pos[0]][curr_pos[1]] = "OO"
                    self.path.append(left)
                    self.findPath(left)
                    block = False
            # else:
            #     self.maze[curr_pos[0]][curr_pos[1]] = "XX"
        except IndexError:
            pass
        if block:
            return -1


maze = Maze(5, 5)
maze.setStart(4, 1)
maze.setExit(3, 4)

maze.setWall(0, 0)
maze.setWall(0, 1)
maze.setWall(0, 2)
maze.setWall(0, 3)
maze.setWall(0, 4)

maze.setWall(1, 0)
maze.setWall(2, 0)
maze.setWall(3, 0)
maze.setWall(4, 0)

maze.setWall(1, 2)
maze.setWall(1, 4)
maze.setWall(2, 4)

maze.setWall(3, 2)
# maze.setWall(3, 3)

maze.setWall(4, 2)
maze.setWall(4, 3)
maze.setWall(4, 4)

# maze.draw()
maze.findPath(maze.start)
maze.draw()

