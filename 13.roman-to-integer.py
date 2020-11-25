'''
Author: your name
Date: 2020-11-25 15:02:10
LastEditTime: 2020-11-25 15:02:10
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/13.roman-to-integer.py
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        roman = 0
        for i in range(len(s)-1):
            if dict[s[i]]<dict[s[i+1]]:
                roman -= dict[s[i]]
            else:
                roman += dict[s[i]]
            
            
        return roman+dict[s[-1]]