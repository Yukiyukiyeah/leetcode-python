'''
@Author: your name
@Date: 2020-05-10 23:26:13
@LastEditTime: 2020-05-10 23:38:18
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode-python/58.length-of-last-word.py
'''
#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # print(s.split(' '))
        if not s: return 0
        split = s.rstrip().split(' ') 
        return len(split[-1])
# @lc code=end

