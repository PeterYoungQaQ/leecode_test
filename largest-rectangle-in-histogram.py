# coding=utf-8
# @Time: 3/18/2019 2:23 PM
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        i = 0
        n = len(heights)
        if n == 0:
            return 0
        if n == 1:
            return heights[0]
        heights.append(0)
        stack = []
        ans = 0
        while i < len(heights):
            if len(stack) == 0 or heights[stack[-1]] <= heights[i]:
                stack.append(i)
                i += 1
            else:
                now_index = stack.pop()
                if len(stack) == 0:
                    ans = max(ans, i * heights[now_index])
                else:
                    ans = max(ans, (i - stack[-1] - 1) * heights[now_index])
        return ans


print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))
