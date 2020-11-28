'''
Author: your name
Date: 2020-11-28 16:58:50
LastEditTime: 2020-11-28 16:58:50
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/57.insert-interval.py
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]
        l, r = [], []
        for interval in intervals:
            if interval[1] < newInterval[0]:
                l.append(interval)
            elif interval[0] > newInterval[1]:
                r.append(interval)
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        return l + [newInterval] + r