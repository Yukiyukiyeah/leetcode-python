'''
Author: your name
Date: 2020-11-23 15:05:48
LastEditTime: 2020-11-23 15:05:49
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/11.container-with-most-water.py
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        if r == 1:
            return min(height[l],height[r])
        maxarea = 0
        while l < r:
            if height[l] < height[r]:
                area = height[l] * (r - l)
                l += 1
            elif height[l] > height[r]:
                area = height[r] * (r - l)
                r -= 1
            else:
                area = height[l] * (r - l)
                l += 1
                r -= 1
            maxarea = max(area, maxarea)
        return maxarea