# coding=utf-8
# @Time: 3/18/2019 2:56 PM
from typing import List


class Solution:
    def __init__(self):
        self.ans = 0

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        if n == 0:
            return 0
        m = len(matrix[0])
        h = [0] * (m + 1)

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    h[j] += 1
                else:
                    h[j] = 0
            self.ans = self.robot(self.ans, h)
        return self.ans

    def robot(self, maxL, h):
        stk = []
        m = len(h) - 1
        i = 0
        while i <= m:
            if len(stk) == 0 or h[stk[-1]] < h[i]:
                stk.append(i)
                i += 1
            else:
                now_idx = stk.pop()
                if len(stk) == 0:
                    maxL = max(maxL, i * h[now_idx])
                else:
                    maxL = max(maxL, (i - stk[-1] - 1) * h[now_idx])
        return maxL


print(Solution().maximalRectangle(
    [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))

