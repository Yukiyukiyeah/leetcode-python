'''
Author: your name
Date: 2020-11-24 14:29:44
LastEditTime: 2020-11-24 14:29:44
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/29.divide-2-integers.py
'''
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        num = dividend / divisor
        if num >= 2**31: num = 2**31 - 1
        if num < -2**31: num = -2**31
        return floor(num) if num >= 0 else ceil(num) 