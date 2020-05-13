'''
@Author: your name
@Date: 2020-05-11 20:16:45
@LastEditTime: 2020-05-11 21:06:11
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode-python/88.merge-sorted-array.py
'''
#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m>0 and n>0:
            if nums1[m-1]>=nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m-=1
            else:
                nums1[m+n-1] = nums2[n-1]
                n-=1
        if n>0:
            nums1[: n] = nums2[: n]
        
        
# @lc code=end

