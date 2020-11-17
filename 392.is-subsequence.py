'''
@Author: your name
@Date: 2020-05-03 14:00:45
LastEditTime: 2020-11-17 17:22:32
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
    '''First, we turned t into a iterator, 
    and what that does is that "c in it" iterates through the iterator 
    until the first position where it finds a match. See here.
    Second, (c in it for c in s) is a generator: it returns an iterator. 
    More about generator here.
    Third, all() has only 1 parenthesis, so syntactic sugar: 
    no need for double parentheses
    all() takes in an iterator as an argument 
    and loops through to find the first False. 
    If it can't find it, it return True. 
    More about all/any and generator here.
'''
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i<len(s) and j<len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
# @lc code=end

