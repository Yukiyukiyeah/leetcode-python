'''
@Author: your name
@Date: 2020-05-09 22:16:30
@LastEditTime: 2020-05-09 22:32:36
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode-python/38.count-and-say.py
'''
#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return '1'
        prev = self.countAndSay(n-1)
        count = 1
        res = ""
        for i in range(len(prev)):
            if i==len(prev)-1 or prev[i]!=prev[i+1] :
                res += str(count) + prev[i]
                count = 1
            else:
                count += 1
        return res

        
# @lc code=end

