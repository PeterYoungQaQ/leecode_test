# coding=utf-8
# @Time: 2/27/2019 1:42 PM
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while 0 < nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(0, len(nums)):
            if nums[i] != (i + 1):
                return i + 1
        return len(nums) + 1


print(Solution().firstMissingPositive([1, 2, 0]))
