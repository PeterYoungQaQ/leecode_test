# coding=utf-8 
# @Time :2018/11/20 9:18
"""
    给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""


# 我的答案
class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s):
        arr = [x for x in s]
        tim = []
        cont = 0
        leng = len(arr)
        for m in s:
            if m.isspace():
                cont += 1
        max = 0
        for i in range(leng):
            if arr[i] not in tim:
                tim.append(arr[i])
                cont += 1
            else:
                if cont >= max:
                    max = cont
                    cont = 0
                    del tim[:]
                    tim.append(arr[i])
                    cont += 1
        print(max)

    lengthOfLongestSubstring(0, "pwwkew")

    # 标准答案
    @staticmethod
    def stan(s):
        # 存储历史循环中最长的子串长度
        max_len = 0
        # 判断传入的字符串是否为空
        if s is None or len(s) == 0:
            return max_len
        # 定义一个字典，存储不重复的字符和字符所在的下标
        str_dict = {}
        # 存储每次循环中最长的子串长度
        one_max = 0
        # 记录最近重复字符所在的位置+1
        start = 0
        for i in range(len(s)):
            # 判断当前字符是否在字典中和当前字符的下标是否大于等于最近重复字符的所在位置
            if s[i] in str_dict and str_dict[s[i]] >= start:
                # 记录当前字符的值+1
                start = str_dict[s[i]] + 1
            # 在此次循环中，最大的不重复子串的长度
            one_max = i - start + 1
            # 把当前位置覆盖字典中的位置
            str_dict[s[i]] = i
            # 比较此次循环的最大不重复子串长度和历史循环最大不重复子串长度
            max_len = max(max_len, one_max)
        return max_len
