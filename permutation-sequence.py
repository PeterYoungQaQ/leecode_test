# coding=utf-8
# @Time: 3/7/2019 10:15 AM


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 0的阶层一直到9！
        fac = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        i = n - 1
        num = list(range(1, n + 1))
        ret = ""
        while i >= 0:
            a, b = k // fac[i], k % fac[i]
            if b == 0:
                a -= 1

            if a >= 0:
                ret += str(num[a])
                del num[a]
                i -= 1
            k = b

            if b == 0:
                for i in reversed(num):
                    ret += str(i)
                break
        return ret