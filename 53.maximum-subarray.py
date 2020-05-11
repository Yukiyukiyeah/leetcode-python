'''
@Author: your name
@Date: 2020-05-09 22:32:54
@LastEditTime: 2020-05-09 22:37:41
@LastEditors: your name
@Description: In User Settings Edit
@FilePath: /leetcode-python/53.maximum-subarray.py
'''
#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i] = max(nums[i], nums[i-1] + nums[i])
        return max(nums)
# @lc code=end

