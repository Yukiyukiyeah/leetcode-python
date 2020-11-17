'''
Author: your name
Date: 2020-11-17 19:57:19
LastEditTime: 2020-11-17 20:06:49
LastEditors: Please set LastEditors
Description: In User Settings Edit

FilePath: /leetcode-python/leetcode-python/1011.capacity-to.py
'''
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l = max(weights)
        r = sum(weights)
        
        while l <= r:
            mid = l + (r - l) // 2
            cur = 0
            need = 1
            for w in weights:
                if cur + w > mid:
                    need += 1
                    cur = 0
                cur += w
            if need > D:
                l = mid + 1
            else:
                r = mid - 1
        return l