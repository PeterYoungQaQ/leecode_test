# coding=utf-8
# @Time: 3/1/2019 12:35 PM


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp表，以p字符串作为列，以s作为行
        dp = [[False for i in range(len(p) + 1)] for j in range(len(s) + 1)]
        # 双方都是空字符串，当然是true
        dp[0][0] = True

        for i in range(1, len(p) + 1):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 1]  # 探讨的是当s为空字符串时候，p的前j项是否匹配
                # 如果p的这一次对应的项是*，则看他前一项是否匹配，如果是其他，还是false
        # 我们没有考虑s不为空，p为空的情况，因为这样会刚好符合默认，也就是全部为false

        # 把字符串想象成未完成的状态，因为动态规划本身其实是不断在建设字符串的
        # 所以p[j-1]为p的最后一项，因为后面的还没有建设

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                # 如果我们最后一项为*
                if p[j - 1] == '*':
                    # 第一：有可能代表空字符串
                    # 第二：有可能就代表一个字符串，就是对应的那个
                    # 第三：有可能代表多个字符
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j - 1] or dp[i - 1][j]
                else:
                    # 如果我们这一项是其他的东西，包括字母或者“”“”“”“”“”"?"
                    # 必须要求各后退一步也能匹配，并且在这号位也能匹配上
                    dp[i][j] = (s[i - 1] == p[j - 1] or p[j - 1] == '?') and dp[i - 1][j - 1]
        # 返回前len(s)的s与前len(p)的匹配结果
        return dp[len(s)][len(p)]


print(Solution().isMatch("ggs", "*s"))
