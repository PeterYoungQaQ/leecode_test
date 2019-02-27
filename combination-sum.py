# coding=utf-8
# @Time: 2/27/2019 12:32 PM
from typing import List


class Solution:
    def DFS(self, candidates, target, start, valuelist):
        if target == 0:
            return Solution.analist.append(valuelist)
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                return
            self.DFS(candidates, target - candidates[i], i, valuelist + [candidates[i]])

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        Solution.analist = []
        self.DFS(candidates, target, 0, [])
        return Solution.analist


print(Solution().combinationSum([2, 3, 5], 8))
