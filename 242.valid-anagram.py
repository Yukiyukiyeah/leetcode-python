'''
@Author: your name
@Date: 2020-05-03 20:55:04
@LastEditTime: 2020-05-04 14:51:01
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode-python/242.valid-anagram.py
'''
#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=star
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1, dic2 = {}, {}
        for item in s:
            dic1[item] = dic1.get(item, 0)+1
        for item in t:
            dic2[item] = dic2.get(item,0)+1
        return dic1 == dic2
        
# @lc code=end

