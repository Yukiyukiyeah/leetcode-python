'''
Author: your name
Date: 2020-11-30 16:00:19
LastEditTime: 2020-11-30 16:00:29
LastEditors: your name
Description: In User Settings Edit
FilePath: /leetcode-python/74.search-a-2d-matrix.py
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        R = len(matrix)
        C = len(matrix[0])
        l = 0
        r = R - 1
        while l <= r:
            mid = l + (r - l) // 2 
            if mid >= R - 1 or matrix[mid][0] < target and matrix[mid + 1][0] > target:
                l2 = 0
                r2 = C - 1
                while l2 <= r2:
                    mid2 = l2 + (r2 - l2) // 2
                    if matrix[mid][mid2] == target: 
                        print(mid, mid2)
                        return True
                    elif matrix[mid][mid2] > target: r2 = mid2 - 1
                    elif matrix[mid][mid2] < target: l2 = mid2 + 1
                break
            elif matrix[mid][0] == target or matrix[mid + 1][0] == target: 
                return True
            elif matrix[mid][0] > target: r = mid - 1
            elif matrix[mid + 1][0] < target: l = mid + 1
        return False