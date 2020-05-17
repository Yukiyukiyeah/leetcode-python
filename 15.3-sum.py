'''
@Author: your name
@Date: 2020-05-03 22:15:19
@LastEditTime: 2020-05-15 18:09:25
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /tencent/Users/yuki/leetcode-python/15.3-sum.py
'''
#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3:
            return None
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left<right:
                cur_sum =  nums[i] + nums[left]+ nums[right]
                if cur_sum < 0:
                    left+=1
                elif cur_sum >0:
                    right-=1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left+=1
                    while left < right and nums[right] == nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
        return res

# @lc code=end

