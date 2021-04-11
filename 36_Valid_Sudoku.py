"""
36. Valid Sudoku
Medium
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example 1:
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
"""
class Solution:
    # brute-force time O(n2), space O(1)
    def isValidSudokuV1(self, board: List[List[str]]) -> bool:
        def tryGet(elem):
            return 0 if elem == "." else int(elem) # 0 signifies invalid entry
        
        def isValidSudoku3x3(board, startX, startY):
            counter = [0] * 10
            for i in range(startX, startX+3):
                for j in range(startY, startY+3):
                    num = tryGet(board[i][j])
                    counter[num] += 1
            for i in range(1, 10):
                if counter[i] > 1:
                    return False
            return True
        
        def isValidSudoku9x9(board):
            for i in range(9):
                for j in range(9):
                    num = tryGet(board[i][j])
                    if num > 0:
                        for col in range(j+1, 9):
                            if tryGet(board[i][col]) == num:
                                return False
                        for row in range(i+1, 9):
                            if tryGet(board[row][j]) == num:
                                return False
            return True
        
        # driver logic

        # validate overall 9x9 grid
        valid = isValidSudoku9x9(board)
        if not valid:
            return False
        
        # validate 3x3 sub-grids
        for i in range(0, len(board), 3):
            for j in range(0, len(board[i]), 3):
                valid = isValidSudoku3x3(board, i, j)
                if not valid:
                    return False
        # if we reached thus far, grid is valid
        return True
    
    # optimized time O(n), space O(1)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [collections.defaultdict(int) for i in range(9)]
        columns = [collections.defaultdict(int) for i in range(9)]
        boxes = [collections.defaultdict(int) for i in range(9)]
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    box_idx = (i // 3) * 3 + (j // 3)
                    rows[i][num] += 1
                    columns[j][num] += 1
                    boxes[box_idx][num] += 1
                    
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_idx][num] > 1:
                        return False
        return True
