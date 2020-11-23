'''
Author: your name
Date: 2020-11-23 16:09:51
LastEditTime: 2020-11-23 16:09:51
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/12. integer-to-roman.py
'''
class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ''
        r = {1000:'M', 
             900:'CM', 500:'D', 400:'CD', 100:'C', 
             90:'XC', 50:'L', 40:'XL', 10:'X', 
             9:'IX', 5:'V', 4:'IV', 1:'I'}
        for k in r:
            while num >= k:
                ans += r[k]
                num -= k
        return ans