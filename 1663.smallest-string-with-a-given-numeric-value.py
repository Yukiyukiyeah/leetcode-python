'''
Author: your name
Date: 2020-11-22 21:50:40
LastEditTime: 2020-11-22 21:50:55
LastEditors: your name
Description: In User Settings Edit
FilePath: /leetcode-python/1663.smallest-string-with-a-given-numeric-value.py
'''
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        '''
        a as much as possible
        '''
        if 26 * n <  k: return None
        if n == 1: return chr(96 + k)
        res = ['a'] * n
        k  = k - n
        for i in range(n-1, -1, -1):
            char = min(k, 25)
            res[i] = chr(97 + char)
            k -= char
            if k <= 0: break
            
        return ''.join(res)