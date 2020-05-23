'''
@Author: your name
@Date: 2020-05-21 14:48:18
@LastEditTime: 2020-05-21 15:00:12
@LastEditors: Please set LastEditors
@Description: In User Settings E
@FilePath: /leetcode-python/547.friend-circles.py
'''
#
# @lc app=leetcode id=547 lang=python3
#
# [547] Friend Circles
#

# @lc code=start
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        seen = set()
        def dfs(node):
            for num, status in enumerate(M[node]):
                if status and num not in seen:
                    seen.add(num)
                    dfs(num)
        res = 0
        for i in range(n):
            if i not in seen:
                dfs(i)
                res += 1
        return res
                    

# @lc code=end

