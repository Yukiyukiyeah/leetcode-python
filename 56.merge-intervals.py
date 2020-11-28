'''
Author: your name
Date: 2020-11-28 15:53:52
LastEditTime: 2020-11-28 15:53:53
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/56.merge-intervals.py
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        intervals.sort(key = lambda interval: interval[0])
        res = []
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr[0] <= res[-1][1]:
                if curr[1] > res[-1][1]:
                    res[-1][1] = curr[1]
            else: res.append(curr)
        return res