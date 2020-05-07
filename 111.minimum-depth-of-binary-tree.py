'''
@Author: your name
@Date: 2020-05-06 19:36:20
@LastEditTime: 2020-05-06 19:40:04
@LastEditors: Please set LastEditors
@Description: In User Settings Edi
@FilePath: /Webdesign/Users/yuki/leetcode-python/111.minimum-depth-of-binary-tree.py
'''
#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        if not root.left and not root.right: return 1
        if not root.left: return self.minDepth(root.right)+1
        if not root.right: return self.minDepth(root.left)+1
        return min(self.minDepth(root.left), self.minDepth(root.right))+1
# @lc code=end

