'''
Author: your name
Date: 2020-12-01 16:39:40
LastEditTime: 2020-12-01 16:41:08
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/213.house-robber-II.py
Solution:
Divide the question into 2 parts: [0, len(nums) - 1), [1, len(nums))
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        
        def rob1(nums, start, end):
            pre = 0
            cur = 0
            for i in range(start, end):
                tmp = cur
                cur = max(cur, pre + nums[i])
                pre = tmp
            return cur
        
        return max(rob1(nums, 0, len(nums) - 1), rob1(nums, 1, len(nums)))
        