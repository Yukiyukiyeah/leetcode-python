'''
@Author: your name
@Date: 2020-05-12 22:49:55
@LastEditTime: 2020-05-12 23:04:40
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /tencent/Users/yuki/leetcode-python/36.valid-sudoku.py
'''
#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        big = set()
        for i in range(9):
            for j in range(9):
                if board[i][j]!=".":
                    cur = board[i][j]
                    if (cur, i) in big or (j, cur) in big or (cur, i//3, j//3) in big:
                        return False
                    big.add((cur, i))
                    big.add((j, cur))
                    big.add((cur, i//3, j//3))
        return True
        
# @lc code=end

