'''
Sudoku Background
Sudoku is a game played on a 9x9 grid. The goal of the game is to fill all cells of the grid with digits from 1 to 9, so that each column, each row, and each of the nine 3x3 sub-grids (also known as blocks) contain all of the digits from 1 to 9.
(More info at: http://en.wikipedia.org/wiki/Sudoku)

Sudoku Solution Validator
Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board, and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's, which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.

The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.

Examples
validSolution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
]); // => true
validSolution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2], 
  [6, 7, 2, 1, 9, 0, 3, 4, 8],
  [1, 0, 0, 3, 4, 2, 5, 6, 0],
  [8, 5, 9, 7, 6, 1, 0, 2, 0],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 0, 1, 5, 3, 7, 2, 1, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 0, 0, 4, 8, 1, 1, 7, 9]
]); // => false
'''

def valid_solution(board):
    total = 0
    zipped = list(zip(*board[::-1]))
    split1,split2,split3 = board[slice(0,3)],board[slice(3,6)], board[slice(6,9)]
    split1,split2,split3 = list(zip(*split1[::-1])),list(zip(*split2[::-1])),list(zip(*split3[::-1]))
    split11,split12,split13 = list(split1[slice(0,3)]), list(split1[slice(3,6)]), list(split1[slice(6,9)])
    split21,split22,split23 = list(split2[slice(0,3)]), list(split2[slice(3,6)]), list(split2[slice(6,9)])
    split31,split32,split33 = list(split3[slice(0,3)]), list(split3[slice(3,6)]), list(split3[slice(6,9)])
    splits =[split11,split12,split13,split21,split22,split23,split31,split32,split33]
        
    for x in range(len(board)):
        if 0 in board[x]:
            return False

        if sum(board[x]) != 45:
            return False

        if sum(zipped[x]) != 45:
            return False

        if (sum(splits[x][0]) + sum(splits[x][1]) + sum(splits[x][2])) != 45:
            return False
    
    return True