'''
Author: your name
Date: 2020-11-25 15:03:05
LastEditTime: 2020-11-25 15:03:21
LastEditors: your name
Description: In User Settings Edit
FilePath: /leetcode-python/14.longest-common-prefix.py
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ''
        common = strs[0]
        for s in strs:
            while common!='' and s.startswith(common) == False:
                common = common[:-1]
            if common == '':
                break
            
        return common
        