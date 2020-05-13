'''
@Author: your name
@Date: 2020-05-12 22:03:37
@LastEditTime: 2020-05-12 22:44:15
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Webdesign/Users/yuki/leetcode-python/51.n-queens.py
'''
#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n<1: return []
        self.result = []
        self.col, self.pie, self.na = set(), set(), set()
        self.DFS(n, 0, [])
        print(self.result)
        return self._generate_result(n)

    def DFS(self, n, row, cur_state):
        if row >= n: 
            self.result.append(cur_state)
            return

        for i in range(n):
            if i in self.col or i+row in self.pie or row-i in self.na:
                continue

            self.col.add(i)
            self.pie.add(i+row)
            self.na.add(row-i)

            self.DFS(n, row+1, cur_state+[i])

            self.col.remove(i)
            self.pie.remove(i+row)
            self.na.remove(row-i)

    def _generate_result(self, n):
        board = []
        for item in self.result:
            for i in item:
                board.append('.' * i + 'Q' + '.' * (n-i-1))
        print(board)
        return [board[i: i+n] for i in range(0, len(board), n)]
            

        
# @lc code=end

