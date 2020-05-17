#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        min = prices[0]
        profit = -prices[0]
        for i in range(len(prices)):
            if prices[i] - min > profit:
                profit = prices[i] - min
            if prices[i] < min:
                min = prices[i]
            
        return profit
        
# @lc code=end

