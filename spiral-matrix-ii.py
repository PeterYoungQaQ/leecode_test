# coding=utf-8
# @Time: 3/7/2019 10:07 AM
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for j in range(n)] for i in range(n)]
        top = 0
        bottom = n - 1
        left = 0
        right = n - 1
        count = 1
        while True:
            for i in range(left, right + 1):
                matrix[top][i] = count
                count += 1
            top += 1
            if left > right or top > bottom:
                break
            for i in range(top, bottom + 1):
                matrix[i][right] = count
                count += 1
            right -= 1
            if left > right or top > bottom:
                break
            for j in range(left, right + 1)[::-1]:
                matrix[bottom][j] = count
                count += 1
            bottom -= 1
            if left > right or top > bottom:
                break
            for i in range(top, bottom + 1)[::-1]:
                matrix[i][left] = count
                count += 1
            left += 1
            if left > right or top > bottom:
                break
        return matrix


print(Solution().generateMatrix(4))
