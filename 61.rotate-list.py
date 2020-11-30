'''
Author: your name
Date: 2020-11-30 14:25:37
LastEditTime: 2020-11-30 14:30:36
LastEditors: your name
Description: In User Settings Edit
FilePath: /leetcode-python/61.rotate-list.py
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head: return None
        
        fast, slow = head, head
        length = 1
        
        while fast.next != None:
            fast = fast.next
            length += 1
        fast_pos = k % length
        
        if fast_pos == 0: return head
        for _ in range(length - fast_pos - 1):
            slow = slow.next
            
        newhead = slow.next
        slow.next = None
        fast.next = head
        return newhead