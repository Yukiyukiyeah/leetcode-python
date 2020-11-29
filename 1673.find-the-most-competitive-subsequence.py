'''
Author: your name
Date: 2020-11-29 21:45:56
LastEditTime: 2020-11-29 21:46:05
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/1673.find-the-most-competitive-subsequence.py
'''
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            while ans and nums[i] < ans[-1] and len(ans) + len(nums) - i - 1 >= k:
                ans.pop()
            if len(ans) < k:
                ans.append(nums[i])
        return ans
                