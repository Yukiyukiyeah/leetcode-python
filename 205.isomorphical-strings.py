'''
Author: your name
Date: 2020-11-20 17:05:56
LastEditTime: 2020-11-20 17:06:21
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/205.isomorphical-strings.py
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        return self.isMap(s, t) and self.isMap(t, s)
    
    def isMap(self, s, t):
        strdict = {}
        for i in range(len(s)):
            if s[i] in strdict:
                if t[i] != strdict[s[i]]:
                    return False
            else:
                strdict[s[i]] = t[i]
        return True
            