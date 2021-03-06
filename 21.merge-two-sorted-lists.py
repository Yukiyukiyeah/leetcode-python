'''
@Author: your name
@Date: 2020-05-07 21:40:57
@LastEditTime: 2020-05-07 22:18:21
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode-python/21.merge-two-sorted-lists.py
'''
#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode()
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next
                

# @lc code=end

