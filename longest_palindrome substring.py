# coding=utf-8 
# @Time :2018/11/20 12:35
"""
(最长回文子串)
    给定一个字符串 s，找到 s 中最长的回文子串。
你可以假设 s 的最大长度为 1000。

示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

示例 2：
输入: "cbbd"
输出: "bb"
"""


class Solution:
    # 直接循环处理的结果,但是会超过时间限制
    def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        max_length = 0
        palindromic = ''
        if s == '':
            palindromic = ''
        else:
            if len(s) == 1:
                return s
            for i in range(l):
                for j in range(i + 1, l):
                    is_palindromic = True
                    for k in range(i, int((i + j) / 2) + 1):
                        if s[k] != s[j - k + i]:
                            is_palindromic = False
                            break
                    if is_palindromic and (j - i + 1) > max_length:
                        max_length = j - i + 1
                        palindromic = s[i:j + 1]

            if palindromic == '':
                palindromic = s[0]
        return palindromic

    # print(longestPalindrome('ac'))

    def manacher(self):
        s = '#' + '#'.join(self.string) + '#'  # 字符串处理，用特殊字符隔离字符串，方便处理偶数子串
        lens = len(s)
        f = []  # 辅助列表：f[i]表示i作中心的最长回文子串的长度
        maxj = 0  # 记录对i右边影响最大的字符位置j
        maxl = 0  # 记录j影响范围的右边界
        maxd = 0  # 记录最长的回文子串长度
        for i in range(lens):  # 遍历字符串
            if maxl > i:
                count = min(maxl - i, int(f[2 * maxj - i] / 2) + 1)  # 这里为了方便后续计算使用count，其表示当前字符到其影响范围的右边界的距离
            else:
                count = 1
            while i - count >= 0 and i + count < lens and s[i - count] == s[i + count]:  # 两边扩展
                count += 1
            if (i - 1 + count) > maxl:  # 更新影响范围最大的字符j及其右边界
                maxl, maxj = i - 1 + count, i
            f.append(count * 2 - 1)
            maxd = max(maxd, f[i])  # 更新回文子串最长长度
        return int((maxd + 1) / 2) - 1  # 去除特殊字符

# 动态规划：对任意字符串，如果头和尾相同，那么它的最长回文子串
# 一定是去头去尾之后的部分的最长回文子串加上头和尾。如果头和尾
# 不同，那么它的最长回文子串是去头的部分的最长回文子串和去尾的
# 部分的最长回文子串的较长的那一个。
    def longestPalindrome(s):
        n = len(s)
        maxl = 0
        start = 0
        for i in range(n):
            if i - maxl >= 1 and s[i-maxl-1: i+1] == s[i-maxl-1: i+1][::-1]:
                start = i - maxl - 1
                maxl += 2
                continue
            if i - maxl >= 0 and s[i-maxl: i+1] == s[i-maxl: i+1][::-1]:
                start = i - maxl
                maxl += 1
        return s[start: start + maxl]

    print(longestPalindrome("aaass"))