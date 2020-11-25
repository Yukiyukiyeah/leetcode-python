'''
Author: your name
Date: 2020-11-25 16:13:46
LastEditTime: 2020-11-25 16:13:47
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/47.permutations-II.py
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums: return None
        nums.sort()
        ans = []
        curr = []
        def dfs(nums, d, n, curr, ans):
            if d == n:
                ans.append(curr)
                return
            for i in range(len(nums)):
                if i > 0 and nums[i-1] == nums[i]: continue
                dfs(nums[:i]+nums[i+1:], d+1, n, curr+[nums[i]], ans)
        dfs(nums, 0, len(nums), curr, ans)
        return ans