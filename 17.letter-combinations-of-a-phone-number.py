'''
Author: your name
Date: 2020-11-23 17:58:34
LastEditTime: 2020-11-23 17:58:34
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/17.number-combinations-of-a-phone-number.py
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2':['a','b','c'],
             '3':['d','e','f'],
             '4':['g','h','i'],
             '5':['j','k','l'],
             '6':['m','n','o'],
             '7':['p','q','r','s'],
             '8':['t','u','v'],
             '9':['w','x','y','z']}
        def backtrack(combination, next_digits):
            if len(next_digits) == 0:
                output.append(combination)
            else:
                for char in d[next_digits[0]]:
                    backtrack(combination + char, next_digits[1:])
            
        output = []
        if digits:
            backtrack('',digits)
        return output