'''
@Author: your name
@Date: 2020-05-13 17:25:02
@LastEditTime: 2020-05-13 18:08:59
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /tencent/Users/yuki/leetcode-python/79.word-search.py
'''
#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board: return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def dfs(self, board, i, j, word):
        if len(word) == 0: return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]: return False

        tmp = board[i][j]
        board[i][j] = '#' # has been visited

        res = self.dfs(board, i-1, j, word[1 :]) or \
            self.dfs(board, i, j-1, word[1: ]) or \
            self.dfs(board, i+1, j, word[1: ]) or \
            self.dfs(board, i, j+1, word[1 :])
    
        # if res: print(i, j)

        board[i][j] = tmp # recursion completed, another branch
        return res

# @lc code=end

