'''
Author: your name
Date: 2020-11-13 21:09:25
LastEditTime: 2020-11-13 21:09:34
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/leetcode-python/190.reverse-bits.py
'''
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = (res << 1) | (n & 1)
            n = n >> 1
        return res