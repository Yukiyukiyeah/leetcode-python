'''
Author: your name
Date: 2020-11-30 14:46:25
LastEditTime: 2020-11-30 14:46:26
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/71.simplify-path.py
'''
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for s in path.split('/'):
            if s == "..":
                if stack:
                    stack.pop()
            elif s and s != '.':
                stack.append(s)
        return '/' + '/'.join(stack)
            