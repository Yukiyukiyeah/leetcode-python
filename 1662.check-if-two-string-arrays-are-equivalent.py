'''
Author: your name
Date: 2020-11-22 13:13:24
LastEditTime: 2020-11-22 13:14:23
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/1662.check-if-two-string-arrays-are-equivalent.py
'''
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)