'''
Author: your name
Date: 2020-11-17 18:51:34
LastEditTime: 2020-11-17 18:52:35
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/leetcode-python/704.binary-search.py
'''
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None:
            return -1
        right = len(nums) - 1
        left = 0
        while left<=right:
            pivot = (left + right)//2
            if target == nums[pivot]:
                return pivot
            if target<nums[pivot]:
                right = pivot - 1gi
            if target>nums[pivot]:
                left = pivot + 1
        return -1
            