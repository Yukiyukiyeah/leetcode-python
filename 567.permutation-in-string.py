'''
Author: your name
Date: 2020-11-16 17:50:04
LastEditTime: 2020-11-16 17:50:25
LastEditors: your name
Description: In User Settings Edit
FilePath: /leetcode-python/leetcode-python/567.permutation-in-string.py
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        print(need)
        l,r = 0, 0
        window = {}
        valid = 0
        while r<len(s2):
            c = s2[r]
            r += 1
            if c in need:
                window[c] = window.get(c,0)+1
                if window[c] == need[c]:
                    valid += 1
            while r-l >= len(s1):
                if valid == len(need):
                    return True
                d = s2[l]
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
                l += 1
        return False