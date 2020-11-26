'''
Author: your name
Date: 2020-11-26 22:39:38
LastEditTime: 2020-11-26 22:39:38
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/461.hamming-distance.py
'''
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = bin(x^y)
        return a.count('1')