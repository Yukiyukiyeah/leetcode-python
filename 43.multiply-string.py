'''
Author: your name
Date: 2020-11-27 15:51:11
LastEditTime: 2020-11-27 15:51:12
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/43.multiply-string.py
'''
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0': return '0'
        res1, res2 = 0, 0
        for c in num1:
            res1 = res1 * 10 + (ord(c) - ord('0'))
            # print(res1)
        for c in num2:
            res2 = res2 * 10 + (ord(c) - ord('0'))
            # print(res2)
        res = res1 * res2
        ans = ''
        while res:
            ans = ans + (chr(ord('0') + res % 10))
            res //= 10
        return ans[::-1]
            