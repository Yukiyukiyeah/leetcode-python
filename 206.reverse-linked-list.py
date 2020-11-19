'''
Author: your name
Date: 2020-11-10 07:31:09
LastEditTime: 2020-11-19 21:10:59
LastEditors: Please set LastEditors
Description: In User Settings Edi
FilePath: /leetcode-python/206.reverse-linked-list.py
'''
#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last
# @lc code=end

