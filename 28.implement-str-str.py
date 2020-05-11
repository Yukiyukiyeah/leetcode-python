'''
@Author: your name
@Date: 2020-05-07 22:41:37
@LastEditTime: 2020-05-07 22:57:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode-python/28.implement-str-str.py
'''
#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
# @lc code=end

