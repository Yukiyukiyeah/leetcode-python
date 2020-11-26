'''
Author: your name
Date: 2020-11-26 22:43:30
LastEditTime: 2020-11-26 22:43:31
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/237.delete-node-in-a-linked-list.py
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        