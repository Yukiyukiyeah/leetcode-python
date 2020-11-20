'''
Author: your name
Date: 2020-11-20 15:32:38
LastEditTime: 2020-11-20 15:32:39
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/202.happy-number.py
'''
class Solution:
    def isHappy(self, n: int) -> bool:
        def add_digit(num):
            res = 0
            while num > 0:
                res += (num % 10) ** 2
                num = num // 10
            return res
        if n == 1: return True
        ans = set()
        while n:
            if n == 1:
                return True
            if n in ans: return False
            ans.add(n)
            n = add_digit(n)