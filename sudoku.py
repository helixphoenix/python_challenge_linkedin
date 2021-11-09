
#This one is from the course

from itertools import product
from typing import List


def sudoku_solver(puzzle: List[List[int]]) -> List[List[int]]:
    for (row, column) in product(range(0,9), repeat=2):  #repeat 2 because row and column are both in range of 0,9
        if puzzle[row][column]==0:
            for num in range(1,10): #possible values for sudoku cells
                allowed = True
#Check column and row for the num
                for i in range(0,9): # checking both its column and rows for the num
                    if (puzzle[i][column]==num)or (puzzle[row][i]==num):
                        allowed=False
                        break # to try another number
# Check the 3X3 unit that the 0 is in
                for (i,j) in product(range(0,3),repeat=2):
                    if puzzle[row-row%3+i][column-column%3+j]== num: # %3+k is the rule for the numbers constructing the box example box:[[(6,6),(6,7),(6,8)],[(7,6),(7,7),(7,8)],[(8,6),(8,7),(8,8)]] 
                        allowed=False
                        break
                
                if allowed:
                    puzzle[row][column]= num
                    if sudoku_solver(puzzle):
                        return sudoku_solver(puzzle)
                    else:
                        puzzle[row][column]= 0
                        
            return False
                           
    return print(puzzle)            

                
                
puzzlek=[[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],[8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],[0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]]


sudoku_solver(puzzlek)