'''
Author: your name
Date: 2020-11-16 15:42:17
LastEditTime: 2020-11-16 15:42:17
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/leetcode-python/76.minimum-window-substring.py
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need  = dict()
        window = {}
        need = Counter(t)
        l, r = 0, 0
        valid = 0
        start = 0
        length = math.inf
        
        s_filtered = []
        for i, char in enumerate(s):
            if char in need:
                s_filtered.append((i, char))
        # print(s_filtered)
        while r<len(s_filtered):
            c = s_filtered[r][1]
            window[c] = window.get(c,0)+1
            if window[c] == need[c]:
                valid += 1
            # print(l, r, window)
            while valid == len(need) and l<=r:
                if s_filtered[r][0] - s_filtered[l][0]+1 < length:
                    start = s_filtered[l][0]
                    length = s_filtered[r][0] - s_filtered[l][0]+1
                    print(length)
                d = s_filtered[l][1]
                if window[d] == need[d]:
                    valid -= 1
                window[d] -= 1    
                l+=1
            r+=1
            
        if length == math.inf: return ""
        return s[start:start+length]