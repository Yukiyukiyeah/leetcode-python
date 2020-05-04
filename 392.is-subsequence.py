#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    '''First, we turned t into a iterator, 
    and what that does is that "c in it" iterates through the iterator 
    until the first position where it finds a match. See here.
    Second, (c in it for c in s) is a generator: it returns an iterator. 
    More about generator here.
    Third, all() has only 1 parenthesis, so syntactic sugar: 
    no need for double parentheses
    all() takes in an iterator as an argument 
    and loops through to find the first False. 
    If it can't find it, it return True. 
    More about all/any and generator here.
'''
    def isSubsequence(self, s: str, t: str) -> bool:
         for i in range (0, len(s)):    
             try:
                 index = t.index(s[i])
             except ValueError: 
                 return False

             t = t[index+1:]

         return True
# @lc code=end

