# coding=utf-8
# @Time: 3/19/2019 2:30 PM
from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        i = 0
        while i < n:
            res_inv = res[::-1]
            res_inv = [x + pow(2, i) for x in res_inv]
            res = res + res_inv
            i += 1
        return res


print(Solution().grayCode(2))
