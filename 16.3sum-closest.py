'''
Author: your name
Date: 2020-11-23 17:20:05
LastEditTime: 2020-11-23 17:20:26
LastEditors: your name
Description: In User Settings Edit
FilePath: /leetcode-python/16.3sum-closest.py
'''

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result = nums[0] + nums[1] + nums[2]
        nums.sort()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(s - target) < abs(result - target):
                    result = s
                if s < target:
                    l += 1
                elif s > target:
                    r-= 1
                else: return result
        return result