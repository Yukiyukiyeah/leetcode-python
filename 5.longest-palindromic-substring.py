'''
Author: your name
Date: 2020-11-15 23:14:35
LastEditTime: 2020-11-15 23:14:58
LastEditors: your name
Description: In User Settings Edit
FilePath: /leetcode-python/leetcode-python/5.longest-palindromic-substring.py
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def getLen(l, r):
            while l>=0 and r<n and s[l] == s[r]:
                l-=1
                r+=1
            return r-l-1
        start = 0
        length = 0
        for i in range(n):
            cur = max(getLen(i, i), getLen(i, i+1))
            if cur <= length:
                continue
            length = cur
            start = i - (cur-1)//2
        return s[start:start+length]