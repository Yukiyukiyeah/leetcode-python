'''
Author: your name
Date: 2020-11-10 07:31:09
LastEditTime: 2020-11-18 20:31:44
LastEditors: your name
Description: In User Settings Edit
FilePath: /leetcode-python/leetcode-python/141.linked-list-cycle.py
'''
#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head
        while fast and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if(slow == fast):
                return True
        return False
# @lc code=end

