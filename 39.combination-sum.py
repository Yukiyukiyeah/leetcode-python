'''
Author: your name
Date: 2020-11-25 14:25:44
LastEditTime: 2020-11-25 14:56:58
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/39.combination-sum.py
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates: return None
        res = []
        def dfs(candidates, begin, target, path, res):
            if target == 0:
                res.append(path)
                return
            for index in range(begin, len(candidates)):
                if candidates[index] > target: continue
                dfs(candidates, index, target - candidates[index], path + [candidates[index]], res)
        dfs(candidates, 0, target, [], res)
        return res