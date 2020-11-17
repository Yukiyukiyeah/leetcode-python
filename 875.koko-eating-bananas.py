'''
Author: your name
Date: 2020-11-17 19:28:34
LastEditTime: 2020-11-17 19:28:50
LastEditors: your name
Description: In User Settings Edit
FilePath: /leetcode-python/leetcode-python/875.koko-eating-bananas.py
'''
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def possible(K):
            sum = 0
            for p in piles:
                sum += (p-1)//K + 1
            return sum <= H
        
        l = 1
        r =  max(piles)
        while l<=r:
            mid = l + (r - l) // 2
            if not possible(mid):
                l = mid + 1
            else: 
                r = mid - 1
        return l
    
        