# coding=utf-8
# @Time: 2/27/2019 12:48 PM
from typing import List


class Solution:
    def Slover(self, candidates, target, res, path, idx):
        for i in range(idx, len(candidates)):
            new_target = target - candidates[i]
            if new_target < 0:
                return
            else:
                if new_target == 0:
                    res.append(path + [candidates[i]])
                else:
                    idx = idx + 1
                    if idx < len(candidates):
                        self.Slover(candidates, new_target, res, path + [candidates[i]], idx)
                    else:
                        return

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        idx = 0
        candidates = sorted(candidates)
        self.Slover(candidates, target, res, path, idx)
        ud_res = []
        for r in res:
            if r not in ud_res:
                ud_res.append(r)
        return ud_res


print(Solution().combinationSum2([2, 3, 2, 5, 1], 9))
