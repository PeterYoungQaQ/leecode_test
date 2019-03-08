# coding=utf-8
# @Time: 3/8/2019 2:25 PM
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        # 先把横行和竖行填好
        for i in range(m):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = 1
            else:  # 督导障碍物就跳出，因为后面的都是0
                break

        for i in range(n):
            if obstacleGrid[0][i] != 1:
                dp[0][i] = 1
            else:
                break

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # 返回最后一个值
        return dp[m - 1][n - 1]


print(Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
