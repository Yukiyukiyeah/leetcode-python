'''
@Author: your name
@Date: 2020-05-04 13:26:13
@LastEditTime: 2020-05-04 14:46:47
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /tencent/Users/yuki/leetcode-python/18.4-sum.py
'''
#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-3):
            if i==0 or nums[i]!=nums[i-1]:
                threesum = self.threeSum(nums[i+1:], target - nums[i])
                #print(threesum)
                for item in threesum:
                    res.append([nums[i]]+item)
        return res
        
    def threeSum(self, nums, target):
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i==0 or nums[i]!=nums[i-1]:
                left = i+1
                right = len(nums) - 1
                t = target - nums[i]
                while left<right:
                    s = nums[left] + nums[right]
                    if s<t:
                        left+=1
                    elif s>t:
                        right-=1
                    else:
                        res.append([nums[i],nums[left],nums[right]])
                        while(left<right and nums[left+1]==nums[left]):
                            left+=1
                        while(left<right and nums[right-1]==nums[right]):
                            right-=1
                        left+=1
                        right-=1
        return res
# @lc code=end

