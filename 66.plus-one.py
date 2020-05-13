'''
@Author: your name
@Date: 2020-05-10 23:38:55
@LastEditTime: 2020-05-10 23:46:58
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode-python/66.plus-one.py
'''
#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(1, len(digits)+1):
            if digits[-i] < 9:
                digits[-i] += 1
                break
            else:
                digits[-i] = 0
                if i == len(digits): digits.insert(0,'1')
        return digits
                
# @lc code=end

