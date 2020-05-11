'''
@Author: your name
@Date: 2020-05-07 22:25:52
@LastEditTime: 2020-05-07 22:40:54
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode-python/27.remove-element.py
'''
#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = 0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[length] = nums[i]
                length+=1                
        return length
# @lc code=end

