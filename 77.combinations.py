'''
Author: your name
Date: 2020-11-30 16:52:16
LastEditTime: 2020-11-30 16:52:16
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/77.combinations.py
'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        def dfs(n, start, depth, path, res):
            if depth == k:
                res.append(path)
                return
            for index in range(start + 1, n + 1):
                dfs(n, index, depth + 1, path + [index], res)
        dfs(n, 0, 0, path, res)
        return res