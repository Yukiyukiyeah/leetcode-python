#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {
            '}':'{',
            ']':'[',
            ')':'('
        }
        for char in s:
            if char not in dict:
                stack.append(char)
            elif not stack or dict[char]!=stack.pop():
                return False
        return not stack
# @lc code=end

