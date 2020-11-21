'''
Author: your name
Date: 2020-11-21 16:00:20
LastEditTime: 2020-11-21 16:00:30
LastEditors: your name
Description: In User Settings Edit
FilePath: /leetcode-python/8.string-to-integer(atoi).py
'''
class Solution:
    def myAtoi(self, s: str) -> int:
        if not s: return 0
        sign = 1
        i = 0
        res = 0
        max_value = 2**31 - 1
        min_value = -2**31
        while i < len(s) and s[i]  == ' ':
            i += 1
        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        while i < len(s) and s[i] >= '0' and s[i] <= '9':
            if res > max_value // 10 or (res == max_value // 10 and int(s[i]) - 0 > max_value % 10):
                return max_value if sign == 1 else min_value
            res = res * 10 + (int(s[i]) - 0)
            i += 1
        print(sign)
        return res * sign