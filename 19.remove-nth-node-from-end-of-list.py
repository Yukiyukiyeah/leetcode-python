'''
Author: your name
Date: 2020-11-18 20:12:10
LastEditTime: 2020-11-18 20:12:46
LastEditors: your name
Description: In User Settings Edit
FilePath: /leetcode-python/leetcode-python/19.remove-nth-node-from-end-of-list.py
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        l = dummy
        r = dummy
        if r.next is None or r.next.next is None:
            return None
        for i in range(n):
            r = r.next            
        while r.next is not None:
            l = l.next
            r = r.next
        l.next = l.next.next
        return dummy.next
            