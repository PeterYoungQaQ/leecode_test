# coding=utf-8
# @Time: 3/25/2019 5:24 PM


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1, 1, 2]
        if n <= 2:
            return dp[n]
        else:
            dp += [0 for i in range(n - 2)]  # 后面创建多个
            for i in range(3, n + 1):
                for j in range(1, i + 1):
                    # 若n为4：dp[0]*dp[3]+dp[1]*dp[2]+dp[2]*dp[1]+dp[3]*dp[0]
                    dp[i] += dp[j - 1] * dp[i - j]
            return dp[n]
