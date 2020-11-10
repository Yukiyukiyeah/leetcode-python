'''
@Author: your name
@Date: 2020-09-09 23:28:34
@LastEditTime: 2020-09-09 23:41:51
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode-python/1.two-sum.py
'''
#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] in dict:
                return [dict[target-nums[i]],i]
            else:
                dict[nums[i]] = i

        # @lc code=end

