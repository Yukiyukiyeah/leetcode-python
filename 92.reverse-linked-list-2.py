'''
Author: your name
Date: 2020-11-19 21:49:09
LastEditTime: 2020-11-19 21:49:09
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/92.reverse-linked-list-2.py
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head is None: return None
        sentinel = ListNode()
        sentinel.next = head
        pre = sentinel
        for _ in range(1, m):
            pre = pre.next
        prev = pre.next
        cur = prev.next
        for _ in range(m, n):
            next_n = cur.next
            cur.next = prev
            prev = cur
            cur = next_n
        pre.next.next = cur
        pre.next = prev
        return sentinel.next
            
            