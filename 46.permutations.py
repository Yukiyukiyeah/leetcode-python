'''
Author: your name
Date: 2020-11-25 16:07:02
LastEditTime: 2020-11-25 16:07:02
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/46.permutations.py
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        curr = []
        def dfs(nums, d, n, curr, ans):
            if d == n:
                ans.append(curr)
                return
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:], d+1, n, curr+[nums[i]], ans)
        dfs(nums, 0, len(nums), curr, ans)
        return ans