# coding=utf-8
# @Time: 3/13/2019 5:07 PM
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        index = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    index.append((i, j))
        for i, j in index:
            matrix[i] = [0] * len(matrix[i])
            for k in range(len(matrix)):
                matrix[k][j] = 0
        return
