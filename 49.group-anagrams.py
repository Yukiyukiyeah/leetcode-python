'''
Author: your name
Date: 2020-11-27 17:57:35
LastEditTime: 2020-11-27 17:58:24
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/49.group-anagrams.py
'''
class Solution():
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()