'''
@Author: your name
@Date: 2020-05-19 23:36:38
@LastEditTime: 2020-05-19 23:52:25
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode-python/155.min-stack.py
'''
#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#
# 用一个数组永远存着最小值
# @lc code=start
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, x):
        # if stack is empty, set the cur_min as x+1 to garantee we can set the updated min x as x when do the min(x, x+1)
        cur_min = x+1 if self.getMin()==None else self.getMin() 
        self.stack.append((x, min(x,cur_min) ))
        
    def pop(self):
        self.stack.pop()
       
    def top(self):
        return self.stack[-1][0] if self.stack else None

    def getMin(self):
        return self.stack[-1][1] if self.stack else None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

