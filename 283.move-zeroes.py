'''
Author: your name
Date: 2020-11-26 23:20:57
LastEditTime: 2020-11-26 23:20:57
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/283.move-zeroes.py
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2: return
        s = 0
        f = 0
        while f < len(nums) - 1:
            while nums[s] != 0 and nums[f]!= 0 and f < len(nums) - 1:
                s += 1
                f += 1
            while nums[f] == 0 and f < len(nums) - 1: 
                f+= 1
            nums[f], nums[s] = nums[s], nums[f]
            s += 1
            