'''
Author: your name
Date: 2020-12-20 15:55:23
LastEditTime: 2020-12-20 15:55:39
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/J13.py
'''
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        visited = set()
        def dfs(i, j, si, sj):
            if i >= m or j >= n or si + sj > k or (i, j) in visited: return 0
            visited.add((i, j))
            return 1 + dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj) + dfs(i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8)
            
        return dfs(0, 0, 0, 0)