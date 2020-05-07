'''
@Author: your name
@Date: 2020-05-06 20:29:23
@LastEditTime: 2020-05-06 22:05:43
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Webdesign/Users/yuki/leetcode-python/22.generate-parentheses.py
'''
#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.list = []
        self._gen(0,0,n,"")
        return self.list
    def _gen(self, left, right, n, result):
        if left == n and right == n:
            self.list.append(result)
            return 
        if left < n:
            self._gen(left+1, right, n, result+"(")
        if left > right and right < n:
            self._gen(left, right+1, n, result+")")
# @lc code=end

