'''
Author: your name
Date: 2020-11-29 20:59:07
LastEditTime: 2020-11-29 20:59:10
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/1672.richest-customer-wealth.py
'''
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(money) for money in accounts)