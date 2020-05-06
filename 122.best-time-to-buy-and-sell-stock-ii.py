'''
@Author: your name
@Date: 2020-05-05 22:44:32
@LastEditTime: 2020-05-05 22:46:11
@LastEditors: Please set LastEditors
@Description: In User Settings 
@FilePath: /Webdesign/Users/yuki/leetcode-python/122.best-time-to-buy-and-sell-stock-ii.py
'''
#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                maxprofit+=prices[i] - prices[i-1]
        return maxprofit
# @lc code=end

