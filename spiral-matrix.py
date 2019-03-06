# coding=utf-8
# @Time: 3/6/2019 2:13 PM
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        global rightcol, icol
        rown = len(matrix)
        coln = len(matrix[0]) if rown > 0 else 0
        total = rown * coln
        ans = []
        i = 0
        while len(ans) < total:
            for rightcol in range(i, coln - i):
                ans.append(matrix[i][rightcol])
            downrow = -1  # 越界标记
            for downrow in range(i + 1, rown - i):
                ans.append(matrix[downrow][rightcol])
                if downrow == -1:
                    break
                icol = -1
            for icol in range(rightcol - 1, -1 + i, -1):
                ans.append(matrix[downrow][icol])
            if icol == -1:
                break
            for uprow in range(downrow - 1, i, -1):
                ans.append(matrix[uprow][icol])
                i += 1
        return ans


print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
