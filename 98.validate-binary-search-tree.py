'''
@Author: your name
@Date: 2020-05-04 15:05:53
@LastEditTime: 2020-05-04 15:37:43
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /tencent/Users/yuki/leetcode-python/98.validate-binary-search-tree.py
'''
#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        v_min, v_max = -inf, inf
        return self.helper(root, v_min, v_max)
    def helper(self, root, v_min ,v_max):
        if not root:
            return True
        if root.val<=v_min or root.val>=v_max:
            return False
        return self.helper(root.left, v_min, root.val) and self.helper(root.right, root.val, v_max)
# @lc code=end

