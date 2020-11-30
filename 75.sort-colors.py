'''
Author: your name
Date: 2020-11-30 16:32:59
LastEditTime: 2020-11-30 16:32:59
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/75.sort-colors.py
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1: return
        p = 0
        q = 0
        k = len(nums) - 1
        while q <= k:
            if p < q and nums[q] == 0:
                nums[p], nums[q] = nums[q], nums[p]
                p += 1
            elif nums[q] == 2:
                nums[q], nums[k] = nums[k], nums[q]
                k -= 1
            else: 
                q += 1
            