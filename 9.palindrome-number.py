'''
Author: your name
Date: 2020-11-25 15:05:20
LastEditTime: 2020-11-25 15:05:21
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/9.palindrome-number.py
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x>=0:
            rev = 0
            x_change = x
            while x_change:
                rev = int(rev*10 + x_change%10)
                x_change = int(x_change/10)                
            if rev ==x:
                return 1            
        else:
            return 0
        