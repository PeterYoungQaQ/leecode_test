# coding=utf-8
# @Time: 3/15/2019 11:24 AM
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            for temp in res[:]:
                x = temp[:]
                x.append(num)
                res.append(x)
        return res


print(Solution().subsets([1, 2, 3]))
