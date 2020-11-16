'''
Author: your name
Date: 2020-11-16 17:52:01
LastEditTime: 2020-11-16 18:03:00
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/leetcode-python/438.find-all-anagrams-in-a-string.py
'''
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = Counter(p)
        window = {}
        l, r = 0, 0
        valid = 0
        res = []
        while r<len(s):
            char_r = s[r]
            r += 1
            if char_r in need:
                window[char_r] = window.get(char_r, 0) + 1
                if window[char_r] == need[char_r]:
                    valid += 1
            
            while r-l>=len(p):
                if valid == len(need):
                    res.append(l)
                char_l = s[l]
                l += 1
                if char_l in need:
                    if window[char_l] == need[char_l]:
                        valid -= 1
                    window[char_l] -= 1
        return res