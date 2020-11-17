'''
Author: your name
Date: 2020-11-17 18:48:19
LastEditTime: 2020-11-17 18:48:49
LastEditors: your name
Description: In User Settings Edit
FilePath: /leetcode-python/leetcode-python/34.find-first-and-last-positions-of-sorted-array.py
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_left_bound(nums, target):
            l = 0
            r = len(nums) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] > target or nums[mid] == target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
            if l>=len(nums) or nums[l]!=target:
                return -1
            return l
        
        def find_right_bound(nums, target):
            l = 0
            r = len(nums) - 1
            while l<=r:
                mid = l + (r - l) // 2
                if nums[mid] < target or nums[mid] == target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
            if r<0 or nums[r]!=target:
                return -1
            return r
                
        return [find_left_bound(nums, target), find_right_bound(nums, target)]
                
                
        
        