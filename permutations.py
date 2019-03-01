# coding=utf-8
# @Time: 3/1/2019 2:58 PM
from typing import List


class Solution:
    def core(self, mark, nums, curr, outcome):
        if sum(mark) == len(nums):
            outcome.append(curr[:])
        for i in range(len(nums)):
            if mark[i]:
                continue
            curr.append(nums[i])
            mark[i] = True
            self.core(mark, nums, curr, outcome)
            mark[i] = False
            curr.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        mark = [False] * len(nums)
        outcome = []
        curr = []
        self.core(mark, nums, curr, outcome)
        return outcome


print(Solution().permute([1, 2, 3]))
