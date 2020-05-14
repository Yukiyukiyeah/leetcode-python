'''
@Author: your name
@Date: 2020-05-13 19:15:07
@LastEditTime: 2020-05-14 13:55:30
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /tencent/Users/yuki/leetcode-python/212.word-search-ii.py
'''
#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#
# @lc code=start
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]
        self.END_OF_WORD = '#'

        self.result = set()

        if not board or not board[0]: return None
        if not words: return None
        
        # build a Trie with words
        root = {}
        for word in words:
            node = root
            for char in word:
                node = node.setdefault(char, {})
            node[self.END_OF_WORD] = self.END_OF_WORD
        print(root)
        # search
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in root:
                    self.dfs(board, i, j, "", root)
        
        return self.result

    def dfs(self, board, i, j, cur_word, cur_dict):
        cur_word += board[i][j]
        cur_dict = cur_dict[board[i][j]]

        if self.END_OF_WORD in cur_dict:
            self.result.add(cur_word)

        # Backtracking
        tmp = board[i][j]
        board[i][j] = '.'

        for n in range(4):
            x, y = i+self.dx[n], j+self.dy[n]
            if 0<=x<len(board) and 0<=y<len(board[0]) and board[x][y]!='.' and board[x][y] in cur_dict:
                # print(x, y, cur_word, cur_dict)
                self.dfs(board, x, y, cur_word, cur_dict)

        board[i][j] = tmp

# @lc code=end

