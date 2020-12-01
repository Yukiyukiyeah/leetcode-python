'''
Author: your name
Date: 2020-12-01 18:01:46
LastEditTime: 2020-12-01 18:01:47
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/91.decode-ways.py
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1 if s[0]!='0' else 0
        
        for i in range(2, n + 1):
            if 0 < int(s[i - 1]) <= 9:
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2 : i]) <= 26:
                dp[i] += dp[i-2]
        return dp[n]
            
                
            