'''
Author: your name
Date: 2020-12-01 17:05:19
LastEditTime: 2020-12-01 17:06:46
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/78.subsets.py
Solution: using dfs same as combination, iterate at each depth
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not nums: return res
        def dfs(nums, depth, start, curr, res):
            if len(curr) == depth:
                res.append(curr)
                return
            for i in range(start, len(nums)):
                dfs(nums, depth, i + 1, curr + [nums[i]], res)
        for d in range(len(nums) + 1):
            curr =  []
            dfs(nums, d, 0, curr, res)
        return res