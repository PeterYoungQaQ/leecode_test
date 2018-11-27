# coding=utf-8 
# @Time :2018/11/27 10:39
"""
    将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字
形排列。比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
"""


class Solution:
    def convert(s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        str_length = len(s)
        ans = ""
        if numRows <= 1:
            return s
        for i in range(numRows):
            c1 = 2 * numRows - 2 * (i + 1)
            c2 = 2 * i
            cnt = i

            ans += s[cnt]
            while cnt < str_length:
                if c1 != 0:
                    cnt += c1
                    if cnt < str_length:
                        ans += s[cnt]
                if c2 != 0:
                    cnt += c2
                    if cnt < str_length:
                        ans += s[cnt]

        return ans
    # print(convert(0, "LEETCODEISHIRING", 3))