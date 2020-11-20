'''
Author: your name
Date: 2020-11-20 14:25:50
LastEditTime: 2020-11-20 14:26:00
LastEditors: your name
Description: In User Settings Edit
FilePath: /leetcode-python/25.reverse-nodes-in-k-group.py
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head
        if head is None:
            return None
        a = head
        b = head
        for i in range(k):
            if b is None: return head
            b = b.next
        newHead = self.reverse(a, b)
        a.next = self.reverseKGroup(b, k)
        return newHead
            
        
    def reverse(self, a, b):
        prev = None
        cur = a
        nxt = a
        while cur != b:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
    