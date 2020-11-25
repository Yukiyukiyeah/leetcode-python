'''
Author: your name
Date: 2020-11-25 10:19:10
LastEditTime: 2020-11-25 10:19:10
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/33.search-in-rotated-sorted-array.py
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target: return mid
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target <= nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] <= target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1