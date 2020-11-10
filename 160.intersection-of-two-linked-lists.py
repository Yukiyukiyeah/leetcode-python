#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        ptr1 = headA
        ptr2 = headB
        while ptr1!=ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            if ptr1 == ptr2:
                return ptr1
            if not ptr1:
                ptr1 = headB
            if not ptr2:
                ptr2 = headA
        return ptr1
# @lc code=end

