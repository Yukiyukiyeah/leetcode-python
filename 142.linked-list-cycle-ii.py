'''
Author: your name
Date: 2020-11-10 07:31:09
LastEditTime: 2020-11-18 20:36:31
LastEditors: your name
Description: In User Settings Edit
FilePath: /leetcode-python/leetcode-python/142.linked-list-cycle-ii.py
'''
#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None

# @lc code=end

