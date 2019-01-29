# coding=utf-8 
# @Time :2019/1/29 14:06


class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: numtr
        """
        if num > 3999 or num < 1:
            return 0
            # 字典是无序的，所以不使用字典
            # 注意这里一定要是倒序，否则执行会有问题，让数从大往小查找适合的罗马数
        num_tuple = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_tuple = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        # 记录结果的字符串
        result_str = ""
        # 从整数的列表中开始遍历
        for i in range(len(num_tuple)):
            # 从大往小开始判断，num小于当前数则进行下一次循环
            # num大于当前数则进行减法运算，并取出相应位置的Roman数
            while num >= num_tuple[i]:
                num -= num_tuple[i]
                result_str += roman_tuple[i]
        return result_str


print(Solution.intToRoman(0, 1522))


class Solution2:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        curr = 0
        pre = 0
        for i in range(len(s)):
            if s[i] == 'I':
                curr = 1
            elif s[i] == 'V':
                curr = 5
            elif s[i] == 'X':
                curr = 10
            elif s[i] == 'L':
                curr = 50
            elif s[i] == 'C':
                curr = 100
            elif s[i] == 'D':
                curr = 500
            elif s[i] == 'M':
                curr = 1000

            result = result + curr

            if pre < curr:
                result = result - 2 * pre
            pre = curr

        return result
