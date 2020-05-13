'''
@Author: your name
@Date: 2020-05-12 23:04:54
@LastEditTime: 2020-05-12 23:57:50
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /tencent/Users/yuki/leetcode-python/37.sudoku-solver.py
'''
#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or len(board) == 0: return None
        self.solve(board)

    def solve(self, board):
        for i in range(len(board[0])):
            for j in range(len(board)):
                if board[i][j] == ".":
                    for c in range(1, 10):
                        if self.is_valid(c, i, j, board):
                            board[i][j] = str(c)
                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = "."
                    return False
        return True

    def is_valid(self, c, row, col, board):
        for i in range(9):
            if board[i][col]!='.' and board[i][col] == str(c):
                return False
            if board[row][i]!='.' and board[row][i] == str(c):
                return False
            if board[3 * (row//3) + i//3][3 * (col//3) + i%3]!='.' and board[3 * (row//3) + i//3][3 * (col//3) + i%3] == str(c):
                return False
        return True
        

                
# @lc code=end

