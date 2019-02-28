# coding=utf-8
# @Time: 2/28/2019 2:47 PM


class Solution:
    def convert(self, num):
        n = len(num)
        i = 0
        val = 0
        ord_zero = ord('0')
        while i < n:
            val = val * 10 + (ord(num[i]) - ord_zero)
            i += 1

        return val

    def multiply(self, num1, num2):
        n1 = self.convert(num1)
        n2 = self.convert(num2)
        return str(n1 * n2)


print(Solution().multiply('10', '20'))
