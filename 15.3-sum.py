'''
@Author: your name
@Date: 2020-05-03 22:15:19
@LastEditTime: 2020-05-04 14:48:48
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
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            # repeated elements
            if i==0 or nums[i-1]!=nums[i]:
                left, right = i+1, len(nums) - 1
                while left<right:
                    num_sum = nums[i] + nums[left] + nums[right]
                    if num_sum>0:
                        right-=1
                    elif num_sum<0:
                        left+=1
                    else:
                        res.append([nums[i],nums[left],nums[right]])
                        # repeated elements
                        while left<right and nums[left] == nums[left+1]:
                            left+=1
                        while left<right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
        return res
# @lc code=end

