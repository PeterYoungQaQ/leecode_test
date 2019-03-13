# coding=utf-8
# @Time: 3/13/2019 2:54 PM


class Solution:
    def climbStairs(self, n: int) -> int:
        condition = [0] * (n+1)
        condition[0] = 1
        condition[1] = 1
        for i in range(2, n+1):
            condition[i] = condition[i-1] + condition[i-2]
        return condition[n]


print(Solution().climbStairs(5))