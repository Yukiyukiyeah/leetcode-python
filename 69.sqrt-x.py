'''
@Author: your name
@Date: 2020-05-11 19:42:45
@LastEditTime: 2020-05-13 15:46:57
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode-python/69.sqrt-x.py
'''
#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        res = x
        while res * res > x:
            res = int((res + x/res)/2)
        return res    
        
# @lc code=end

