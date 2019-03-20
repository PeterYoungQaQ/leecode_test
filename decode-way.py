# coding=utf-8
# @Time: 3/20/2019 3:48 PM


class Solution:
    def numDecodings(self, s: str) -> int:
        if s == "" or s[0] == "0":
            return 0
        dp = [1, 1]
        for i in range(2, len(s) + 1):
            if 10 <= int(s[i - 2:i]) <= 26 and s[i - 1] != '0':  # 编码方式为2
                dp.append(dp[i - 1] + dp[i - 2])
            elif int(s[i - 2:i]) == 10 or int(s[i - 2:i]) == 20:  # 编码方式为1
                dp.append(dp[i - 2])
            elif s[i - 1] != '0':
                dp.append(dp[i - 1])
            else:
                return 0
        return dp[len(s)]


print(Solution().numDecodings("226"))
