'''
Author: your name
Date: 2020-11-28 15:16:58
LastEditTime: 2020-11-28 15:16:59
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/45.jump-game-II.py
'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        end = 0
        farthest = 0
        jump = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, nums[i] + i)
            if (i == end):
                jump += 1
                end = farthest
        return jump
            