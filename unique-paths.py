# coding=utf-8
# @Time: 3/7/2019 1:41 PM


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        dp = [[1 for _ in range(m)] for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):  # 等于上边和左边的值相加
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


print(Solution().uniquePaths(7, 3))