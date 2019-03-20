# coding=utf-8
# @Time: 3/20/2019 1:54 PM

from typing import List


class Solution:
    @staticmethod
    def subsetsWithDup(nums: List[int]) -> List[List[int]]:
        global num
        all_subsets = [[]]
        nums.sort()
        if nums:
            for i in range(len(nums)):
                # 重复的情况
                if i > 0 and nums[i] == nums[i - 1]:
                    num += 1
                    start = int(len(all_subsets) * (num - 1) / num)
                    for idx in range(start, len(all_subsets)):
                        all_subsets.append(all_subsets[idx] + [nums[i]])
                else:
                    num = 1
                    for idx in range(len(all_subsets)):
                        all_subsets.append(all_subsets[idx] + [nums[i]])
            return all_subsets


print(Solution().subsetsWithDup([1, 2, 2]))
