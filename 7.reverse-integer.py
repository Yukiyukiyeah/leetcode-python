'''
@Author: your name
@Date: 2020-09-09 23:50:05
@LastEditTime: 2020-09-10 00:05:34
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode-python/7.reverse-integer.py
'''
#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if -10<x<10:
            return x
        ans = 0
        flag = 1
        if x<0:
            x = -x
            flag = -flag
        while x!=0:
            cur = x % 10
            ans = ans * 10 + cur
            x //=10
            print(x)
        return ans*flag if -2**31 < ans <2**31 else 0
            
# @lc code=end

