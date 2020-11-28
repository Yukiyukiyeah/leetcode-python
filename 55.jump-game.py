'''
Author: your name
Date: 2020-11-28 14:38:05
LastEditTime: 2020-11-28 14:38:06
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/55.jump-game.py
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = 0
        for i, n in enumerate(nums):
            if i > m: return False
            m = max(m, i + n)
        return True