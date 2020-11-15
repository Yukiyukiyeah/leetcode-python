'''
Author: your name
Date: 2020-11-09 20:45:01
LastEditTime: 2020-11-15 21:54:08
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/leetcode-python/3.longest-substring-without-repeating-characters.py
'''
#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        if len(s) == 0:return ans
        max_dict = dict()
        i = 0
        for j in range(len(s)):
            if s[j] in max_dict:
                i = max(i, max_dict.get(s[j])+1)
            ans = max(ans, j-i+1)
            max_dict[s[j]] = j
        return ans
                
        
        
        
# @lc code=end

