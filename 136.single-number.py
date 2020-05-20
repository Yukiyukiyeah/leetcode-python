'''
@Author: your name
@Date: 2020-05-18 19:45:26
@LastEditTime: 2020-05-18 19:56:33
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode-python/136.single-number.py
'''
#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict = {}
        for num in nums:
            dict[num] = dict.get(num, 0) + 1
        for key, val in dict.items():
            if val==1:
                return key
# @lc code=end

