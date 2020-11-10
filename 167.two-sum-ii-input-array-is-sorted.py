'''
Author: your name
Date: 2020-11-10 07:31:09
LastEditTime: 2020-11-10 11:12:23
LastEditors: your name
Description: In User Settings Edit
FilePath: /leetcode-python/leetcode-python/167.two-sum-ii-input-array-is-sorted.py
'''
#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        ptr1 = 0
        ptr2 = len(numbers)-1
        
        while ptr1!=ptr2:
            sum = numbers[ptr1] + numbers[ptr2]
            if sum == target:
                return [ptr1+1, ptr2+1]
            elif sum < target:
                ptr1+=1
            else:
                ptr2-=1
        return None
        
        
# @lc code=end

