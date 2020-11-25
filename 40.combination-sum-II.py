'''
Author: your name
Date: 2020-11-25 14:25:24
LastEditTime: 2020-11-25 14:40:38
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /leetcode-python/40.combination-sum-II.py
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates or sum(candidates)<target: return None
        candidates.sort()
        print(candidates)
        result = []
        def dfs(candidates, begin, end, target, path, result):
            if target == 0:
                result.append(path)
                return
            for index in range(begin, end):
                if candidates[index] > target: return
                if index > begin and candidates[index] == candidates[index - 1]:
                    continue
                dfs(candidates, index+1, end, target - candidates[index], 
                    path + [candidates[index]], result)
        end = len(candidates)
        dfs(candidates, 0, end, target, [], result)
        return result
        
        