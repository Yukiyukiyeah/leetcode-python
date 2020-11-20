'''
Author: your name
Date: 2020-11-20 15:47:38
LastEditTime: 2020-11-20 15:47:38
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/203.remove-linked-list-elements.py
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return head
        sentinel = ListNode(0)
        sentinel.next = head
        ptr = sentinel
        while ptr.next is not None:
            if ptr.next.val == val:
                ptr.next = ptr.next.next
                continue
            ptr = ptr.next
        return sentinel.next
        