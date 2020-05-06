'''
@Author: your name
@Date: 2020-05-05 21:18:47
@LastEditTime: 2020-05-05 22:06:19
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Webdesign/Users/yuki/leetcode-python/169.majority-element.py
'''
#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
# @lc code=end

