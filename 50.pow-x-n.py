'''
@Author: your name
@Date: 2020-05-04 17:25:16
@LastEditTime: 2020-05-04 17:33:41
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /tencent/Users/yuki/leetcode-python/50.pow-x-n.py
'''
#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n: return 1
        if n<0:
            return 1/self.myPow(x,-n)
        if n%2 == 1:
            return self.myPow(x,n-1)*x
        return self.myPow(x*x, n/2)
       

# @lc code=end

