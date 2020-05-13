'''
@Author: your name
@Date: 2020-05-11 20:08:15
@LastEditTime: 2020-05-11 20:16:31
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode-python/83.remove-duplicates-from-sorted-list.py
'''
#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur and cur.next:
            if cur.next.val == cur.val:
                cur.next = cur.next.next
            else:cur = cur.next
        return head
# @lc code=end

