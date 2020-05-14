'''
@Author: your name
@Date: 2020-05-14 13:56:13
@LastEditTime: 2020-05-14 14:02:01
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /tencent/Users/yuki/leetcode-python/191.number-of-1-bits.py
'''
#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n>0:
            n = n&(n-1)
            res +=1
        return res
# @lc code=end

