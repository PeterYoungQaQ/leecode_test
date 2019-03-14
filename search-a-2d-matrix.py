# coding=utf-8
# @Time: 3/14/2019 2:28 PM
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not len(matrix[0]):
            return False
        left = 0
        right = len(matrix) - 1
        while left <= right:
            mid = int((left + right) / 2)  # 只保留整数
            if matrix[mid][0] > target:
                right = mid - 1
            elif matrix[mid][0] < target:
                left = mid + 1
            else:
                return True

        x = left - 1  # 这样出来如果没匹配正好的数，到出循环时就是大于要查找的那个数一位
        left = 0
        right = len(matrix[0]) - 1
        while left <= right:
            mid = int((left + right) / 2)  # 只保留整数
            if matrix[x][mid] > target:
                right = mid - 1
            elif matrix[x][mid] < target:
                left = mid + 1
            else:
                return True
        return False


print(Solution().searchMatrix([[1, 3, 5, 7],
                              [10, 11, 16, 20],
                              [23, 30, 34, 50]], 3))
