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
        cur, prev = head, None
        # 连续赋值等式右边都是局部变量，而非变量值本身
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev
# @lc code=end

