'''
@Author: your name
@Date: 2020-05-13 19:15:07
@LastEditTime: 2020-05-13 20:04:55
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /tencent/Users/yuki/leetcode-python/212.word-search-ii.py
'''
#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#
import collections
# @lc code=start
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]
        
        self.END_OF_WORD = '#'
        self.result = set()

        if not board or not board[0]: return None
        if not words: return None
        
        root = collections.defaultdict()
        for word in words:
            node = root
            for char in word:
                node = node.setdefault(char, collections.defaultdict())
            node[self.END_OF_WORD] = self.END_OF_WORD
        # print(root)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in root:
                    self.dfs(board, i, j, "", root)
                    
        return self.result
                    
    def dfs(self, board, i, j, cur_word, cur_dict):
        cur_word += board[i][j]
        # print(cur_word)
        cur_dict = cur_dict[board[i][j]]

        if self.END_OF_WORD in cur_dict:
            self.result.add(cur_word)
        
        tmp = board[i][j]
        board[i][j] = '.'

        for n in range(4):
            x = i+self.dx[n]
            y = j+self.dy[n]
            # print('after',x, y)
            if x>=0 and x<len(board) and y>=0 and y<len(board[0]) \
                and board[x][y]!='.' and board[x][y] in cur_dict:
                self.dfs(board, x, y, cur_word, cur_dict)
        board[i][j] = tmp

        
        

# @lc code=end

