'''
Author: your name
Date: 2020-11-25 09:53:53
LastEditTime: 2020-11-25 09:54:00
LastEditors: your name
Description: In User Settings Edit
FilePath: /leetcode-python/31.next-permutation.py
'''
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        1 5 8 4 7 6 5 3 1
        """
        def swap(nums, a, b):
            tmp = nums[a]
            nums[a] = nums[b]
            nums[b] = tmp
        def reverse(nums, start):
            i = start
            j = len(nums) - 1
            while i < j:
                swap(nums, i, j)
                i += 1
                j -= 1
        i = len(nums) - 1
        if i == 0: return nums
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0: return nums.sort()
        else:
            cur = nums[i-1]
            j = i
            while j < len(nums) and cur < nums[j] :
                j += 1
            swap(nums, i-1, j-1)
            reverse(nums, i)
            