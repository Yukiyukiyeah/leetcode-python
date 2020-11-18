'''
@Author: your name
@Date: 2020-05-03 14:00:45
LastEditTime: 2020-11-17 20:39:11
LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /tencent/Users/yuki/leetcode-python/392.is-subsequence.py
'''
#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i<len(s) and j<len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
# @lc code=end

