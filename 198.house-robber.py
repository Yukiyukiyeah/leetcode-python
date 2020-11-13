'''
Author: your name
Date: 2020-11-13 21:56:26
LastEditTime: 2020-11-13 21:56:26
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/leetcode-python/198.house-robber.py
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        last, now = 0, 0
        for num in nums:
            last, now = now, max(last+num, now)
        return now
            
