''' Python3 program to solve N Queen Problem using backtracking '''
c = 1
backtrack = 0
global N
N = int(input("Enter dimension of square chess board: "))

# A utility function to print solution
def printSol(board):
    global c
    k=0
    for element in board:
        print(element)
        k += 1
        if k == N:
            c+=1
            print("----------------------------------------")


''' A utility function to check if a queen can be placed on board[row][col]. Note that this 
function is called when "col" queens are already placed in columns from 0 to col -1. 
So we need to check only left side for attacking queens '''


def checkConflicts(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


''' A recursive utility function to solve N Queen problem '''


def solveNQueens(board, col):
    global backtrack
    ''' base case: If all queens are placed then return true '''
    if col == N:
        printSol(board)
        return True

    ''' Consider this column and try placing this queen in all rows one by one '''
    res = False
    for j in range(N):

        ''' Check if queen can be placed on board[i][col] '''
        if checkConflicts(board, j, col):
            # Place this queen in board[i][col]
            board[j][col] = 1

            # Make result true if any placement is possible
            res = solveNQueens(board, col + 1) or res

            ''' If placing queen in board[i][col] doesn't lead to a solution, then 
            remove queen from board[i][col] '''
            board[j][col] = 0  # BACKTRACK
            backtrack += 1

    ''' If queen can not be place in any row in this column col then return false '''
    return res


''' This function solves the N Queen problem using Backtracking. It mainly uses solveNQUtil() to 
solve the problem. It returns false if queens cannot be placed, otherwise return true and 
prints placement of queens in the form of 1s. Please note that there may be more than one 
solutions, this function prints one of the feasible solutions.'''

# Driver Code
board = [[0 for j in range(N)] for i in range(N)]

if solveNQueens(board, 0) is False:
    print("Solution does not exist")


print("No. of backtracks: ", backtrack)
print("No of solutions = ", c-1)
