'''
@Author: your name
@Date: 2020-05-15 14:33:03
@LastEditTime: 2020-05-15 15:23:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /tencent/Users/yuki/leetcode-python/120.triangle.py
'''
#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 也可以用一层数组只存当前层
        n = len(triangle)-1
        res = triangle[n]
        for i in range(n-1, -1, -1):
            for j in range(i+1):
                res[j] = min(res[j], res[j+1]) + triangle[i][j]
            print(res)
                # print(triangle[i][j])
        return res[0]
        
                   
        
# @lc code=end

