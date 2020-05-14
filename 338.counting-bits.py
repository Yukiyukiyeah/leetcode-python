'''
@Author: your name
@Date: 2020-05-14 14:08:07
@LastEditTime: 2020-05-14 14:29:53
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /tencent/Users/yuki/leetcode-python/338.counting-bits.py
'''
#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0]
        while len(res) <= num:
            res+=[i+1 for i in res]
        return res[:num+1]
# @lc code=end

