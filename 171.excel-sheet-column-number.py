'''
Author: your name
Date: 2020-11-10 11:25:35
LastEditTime: 2020-11-10 11:25:43
LastEditors: your name
Description: In User Settings Edit
FilePath: /leetcode-python/leetcode-python/171. Excel Sheet Column Number.py
'''
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        li = []
        li[: 0] = s
        li = li[::-1]
        res = 0
        for i, n in enumerate(li):
            res += pow(26,i)*(ord(n)-64)
            print(i,n)
        return res