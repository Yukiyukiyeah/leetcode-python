'''
Author: your name
Date: 2020-11-26 16:47:54
LastEditTime: 2020-11-26 22:24:27
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/215-kth-largest-element-in-an-array-1.py
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums: return None
        return self.quickselect(nums, 0, len(nums) - 1, k)
        
    def quickselect(self, nums, start, end, k):
        pivot = nums[start]
        # remove bigger number before the pivot, 
        # smaller number behind the pivot
        while start < end:
            while start < end and nums[end] <= pivot:
                end -= 1
            nums[start] = nums[end]
            while start < end and nums[start] > pivot:
                start += 1
            nums[end] = nums[start]
        nums[start] = pivot
        if start == k - 1: return nums[start]
        elif start < k - 1: return self.quickselect(nums, start + 1, len(nums) - 1, k)
        else: return self.quickselect(nums, 0, start - 1, k)
            