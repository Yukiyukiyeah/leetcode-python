'''
@Author: your name
@Date: 2020-05-10 23:47:17
@LastEditTime: 2020-05-10 23:59:11
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode-python/67.add-binary.py
'''
#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ''
        carry = 0

        a = list(a)
        b = list(b)

        while a or b or carry:
            if a : carry += int(a.pop())
            if b: carry += int(b.pop())
            result += str(carry%2)
            if carry //2 == 1: carry = 1
            else: carry = 0

        return result[: : -1]
        
# @lc code=end

