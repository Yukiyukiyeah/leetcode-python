'''
@Author: your name
@Date: 2020-05-14 14:03:34
@LastEditTime: 2020-05-14 14:07:36
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /tencent/Users/yuki/leetcode-python/231.power-of-two.py
'''
#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n!=0 and n&(n-1)==0:
            return True
        return False
# @lc code=end

