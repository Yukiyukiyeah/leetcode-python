'''
Author: your name
Date: 2020-11-27 21:42:26
LastEditTime: 2020-11-27 21:42:26
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/217.contains-duplicate.py
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for n in nums:
            if n in d: return True
            d[n] = 1
        return False
            