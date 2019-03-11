# coding=utf-8
# @Time: 3/11/2019 2:45 PM


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

    def addBinary2(self, a: str, b: str) -> str:
        a = list(a)
        b = list(b)
        carry = 0
        res = ""
        while len(a) != 0 or len(b) != 0:
            if len(a) != 0:
                tmp1 = int(a.pop())
            else:
                tmp1 = 0
            if len(b) != 0:
                tmp2 = int(b.pop())
            else:
                tmp2 = 0
            tmp = divmod(tmp1 + tmp2 + carry, 2)
            carry = tmp[0]
            res = str(tmp[1]) + res
        if carry == 1:
            res = str(carry) + res
        return res


print(Solution().addBinary2("1010", "1011"))
