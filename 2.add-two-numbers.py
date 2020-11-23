'''
Author: your name
Date: 2020-09-08 15:04:43
LastEditTime: 2020-11-23 16:22:25
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/2.add-two-numbers.py
'''
#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode()
        res_ptr = res
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            carry, val = divmod(val1 + val2 + carry, 10)
            res_ptr.next = ListNode(val)
            res_ptr = res_ptr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return res.next
            
# @lc code=end

