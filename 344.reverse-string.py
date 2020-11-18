'''
Author: your name
Date: 2020-11-18 20:49:40
LastEditTime: 2020-11-18 20:49:50
LastEditors: your name
Description: In User Settings Edit
FilePath: /leetcode-python/leetcode-python/344.reverse-string.py
'''
def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s) - 1
        for i in range(len(s)//2):
            tmp = s[i]
            s[i] = s[l-i]
            s[l-i] = tmp