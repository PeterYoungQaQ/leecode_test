# coding=utf-8
# @Time: 3/1/2019 1:47 PM
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        counter = 0
        curr_end = 0
        curr_farthest = 0
        for i in range(len(nums) - 1):
            curr_farthest = max(curr_farthest, i + nums[i])
            if i == curr_end:
                counter += 1
                curr_end = curr_farthest
        return counter


print(Solution().jump([1, 2, 1, 1, 1]))
