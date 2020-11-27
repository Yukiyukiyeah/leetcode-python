'''
Author: your name
Date: 2020-11-27 17:29:02
LastEditTime: 2020-11-27 17:29:02
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/48.rotate-image.py
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        w = len(matrix)
        for i in range(w // 2 + w % 2):
            for j in range(w // 2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[w-1-j][i]
                matrix[w-1-j][i] = matrix[w-1-i][w-1-j]
                matrix[w-1-i][w-1-j] = matrix[j][w-1-i]
                matrix[j][w-1-i] = tmp
            
            
            