'''
@Author: your name
@Date: 2020-05-04 15:41:29
@LastEditTime: 2020-05-04 16:21:09
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /tencent/Users/yuki/leetcode-python/235.lowest-common-ancestor-of-a-binary-search-tree.py
'''
#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val<root.val and q.val<root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val>root.val and q.val>root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root
# @lc code=end

