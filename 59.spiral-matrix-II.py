'''
Author: your name
Date: 2020-11-27 21:21:48
LastEditTime: 2020-11-27 21:21:48
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/59.spiral-matrixII.py
'''
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0]*n for i in range(n)]
        r1 = 0
        r2 = n - 1
        c1 = 0
        c2 = n - 1
        num = 1
        while num <= n**2 and r1 <= r2 and c1 <= c2:
            for c in range(c1, c2 + 1):
                ans[r1][c] = num
                num += 1
            for r in range(r1 + 1, r2 + 1):
                ans[r][c2] = num
                num +=1
            if r1 < r2 and c1 < c2:
                for c in range(c2 - 1, c1, -1):
                    ans[r2][c] = num
                    num += 1
                for r in range(r2, r1, -1):
                    ans[r][c1] = num
                    num += 1
            c1 += 1
            c2 -= 1
            r1 += 1
            r2 -= 1
            
        return ans