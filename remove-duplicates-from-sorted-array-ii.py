# coding=utf-8
# @Time: 3/15/2019 1:28 PM
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        return self.removeDuplicatesHelper(nums, len(nums), 2)

    @staticmethod
    def removeDuplicatesHelper(A, n, k):
        if n <= k:
            return n
        lengthIndex = 1
        cnt = 1
        for j in range(1, n):
            if A[j] != A[j - 1]:
                cnt = 1
                A[lengthIndex] = A[j]
                lengthIndex += 1
            else:
                if cnt < k:
                    A[lengthIndex] = A[j]
                    cnt += 1
                    lengthIndex += 1
        return lengthIndex


print(Solution().removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
