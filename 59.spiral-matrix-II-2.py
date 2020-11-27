'''
Author: your name
Date: 2020-11-27 21:29:31
LastEditTime: 2020-11-27 21:29:41
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/59.spiral-matrix-II2.py
'''
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0]*n for i in range(n)]
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        for i in range(1, n**2 + 1):
            ans[r][c] = i
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < n and 0 <= cc < n and ans[cr][cc] == 0:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return ans