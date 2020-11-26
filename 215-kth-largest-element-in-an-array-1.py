'''
Author: your name
Date: 2020-11-26 16:47:54
LastEditTime: 2020-11-26 16:48:34
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/215-kth-largest-element-in-an-array-1.py
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp = nums[:k]
        heapq.heapify(hp)
        for num in nums[k:]:
            heapq.heappush(hp, num)
            heapq.heappop(hp)
        return hp[0]
            
            