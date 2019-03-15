# coding=utf-8
# @Time: 3/15/2019 11:05 AM
from typing import List


class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        self.helper(range(1, 1 + n), k, 0, path, res)
        return res

    def helper(self, l, k, start_idx, path, res):
        if k == 0:
            res.append(list(path))
            return

        for i in range(start_idx, len(l) - k + 1):
            path.append(l[i])
            self.helper(l, k - 1, i + 1, path, res)
            path.pop()


print(Solution().combine(4, 2))
