'''
Author: your name
Date: 2020-11-22 22:20:08
LastEditTime: 2020-11-22 22:20:18
LastEditors: your name
Description: In User Settings Edit
FilePath: /leetcode-python/1664.ways-to-make-a-fair-array.py
'''
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        res = 0
        s1 = [0, 0]
        s2 = [sum(nums[::2]), sum(nums[1::2])]
        for i, a in enumerate(nums):
            s2[i%2] -= a
            # print(a, s1[0] + s2[1], s1[1] + s2[0])
            res += s1[0] + s2[1] == s1[1] + s2[0]
            s1[i%2] += a
        return res