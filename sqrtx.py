# coding=utf-8
# @Time: 3/12/2019 2:33 PM


class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left < right:
            mid = int((left + right) / 2)
            if x < mid ** 2:
                right = mid
            else:
                left = mid + 1
        if left > 1:
            return left - 1
        else:
            return left

    def mySqrt2_newton(self, x: int) -> int:
        if x == 0:
            return 0
        res = 1
        pre = 0
        while abs(res - pre) > 1e-6:
            pre = res
            res = (res + x / res) / 2

        return int(res)


print(Solution().mySqrt2_newton(8))
