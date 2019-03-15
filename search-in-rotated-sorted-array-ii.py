# coding=utf-8
# @Time: 3/15/2019 2:45 PM
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        pol = len(nums) - 1
        while pol > 0 and nums[pol] >= nums[pol-1]:
            pol -= 1
        ans = self.binary_search(target, nums[:pol])
        if ans == -1:
            ans = self.binary_search(target, nums[pol:])
            if ans != -1:
                return True
            else:
                return False
        else:
            return True

    def binary_search(self, target, nums):
        index = -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                index = mid
                break
        return index

