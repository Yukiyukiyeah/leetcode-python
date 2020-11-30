'''
Author: your name
Date: 2020-11-30 16:08:49
LastEditTime: 2020-11-30 16:09:00
LastEditors: Please set LastEditors
Description: In User Settings Edit

FilePath: /leetcode-python/74.search-matrix2.py
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0] or matrix[-1][-1] < target: return False
        R = len(matrix)
        C = len(matrix[0])
        l = 0
        r = R * C - 1
        while l <= r:
            mid = l + (r - l) // 2
            if matrix[mid // C][mid % C] == target: return True
            elif matrix[mid // C][mid % C] < target:
                l = mid + 1
            elif matrix[mid // C][mid % C]  > target:
                r = mid - 1
        return False