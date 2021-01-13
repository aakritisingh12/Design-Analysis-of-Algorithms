suduko = [[5, 1, 7, 6, 0, 0, 0, 3, 4],
          [2, 8, 9, 0, 0, 4, 0, 0, 0],
          [3, 4, 6, 2, 0, 5, 0, 9, 0],
          [6, 0, 2, 0, 0, 0, 0, 1, 0],
          [0, 3, 8, 0, 0, 6, 0, 4, 7],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 9, 0, 0, 0, 0, 0, 7, 8],
          [7, 0, 3, 4, 0, 0, 5, 6, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]


# creating a printable output of suduko board
def printSuduko(grid):
    for x in range(len(grid)):
        if x % 3 == 0 and x != 0:
            print("- - - - - - - - - - - - -")
        for y in range(len(grid[0])):
            if y % 3 == 0 and y != 0:
                print(" | ", end="")
            if y == 8:
                print(grid[x][y])
            else:
                print(str(grid[x][y]) + " ", end="")


# to find an empty cell in board
def findEmptyCellToFill(grid):
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 0:
                return x, y  # row, columnn
    return None


backtracks = 0


def isvalid(grid, num, pos):
    # Check row
    for i in range(len(grid[0])):
        if grid[pos[0]][i] == num and pos[1] != i:
            return False
    # Check column
    for i in range(len(grid)):
        if grid[i][pos[1]] == num and pos[0] != i:
            return False

    # Check 3*3 box
    xGrid = pos[1] // 3
    yGrid = pos[0] // 3

    for x in range(yGrid * 3, yGrid * 3 + 3):
        for y in range(xGrid * 3, xGrid * 3 + 3):
            if grid[x][y] == num and (x, y != pos):
                return False
    return True


def solveSuduko(grid):
    global backtracks
    findNext = findEmptyCellToFill(grid)
    if not findNext:
        return True
    else:
        row, col = findNext

    for i in range(1, 10):
        if isvalid(grid, i, (row, col)):
            grid[row][col] = i
            if solveSuduko(grid):
                return True
            backtracks += 1
            grid[row][col] = 0
    return False


# Driver Function
printSuduko(suduko)
solveSuduko(suduko)
print("**************************")
printSuduko(suduko)
print("No. of backtracks: ", backtracks)
