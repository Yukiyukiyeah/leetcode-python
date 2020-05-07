'''
@Author: your name
@Date: 2020-05-06 15:53:39
@LastEditTime: 2020-05-06 19:40:41
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Webdesign/Users/yuki/leetcode-python/104.maximum-depth-of-binary-tree.py
'''
#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1

# @lc code=end

