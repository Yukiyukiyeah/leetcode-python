'''
@Author: your name
@Date: 2020-05-19 23:53:09
@LastEditTime: 2020-05-19 23:58:21
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode-python/172.factorial-trailing-zeroes.py
'''
#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0
        while n>0:
            result += n//5
            n//=5
        return result
# @lc code=end

