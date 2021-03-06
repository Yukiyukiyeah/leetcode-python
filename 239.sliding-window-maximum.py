#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums: return None
        window, res = [], []
        for i, x in enumerate(nums):
            if i>=k and window[0]<=i-k:
                window.pop(0)        
            while window and x>=nums[window[-1]]:
                window.pop()
            window.append(i)
            if i>=k-1:
                res.append(nums[window[0]])
        return res
        
# @lc code=end

