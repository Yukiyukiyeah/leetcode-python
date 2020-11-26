'''
Author: your name
Date: 2020-11-26 23:29:06
LastEditTime: 2020-11-26 23:29:06
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/258.add-digits.py
'''
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0: return 0
        return (num - 1) % 9 + 1