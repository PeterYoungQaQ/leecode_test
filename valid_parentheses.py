# coding=utf-8 
# @Time :2019/2/2 12:08


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1 or len(s) == 0:
            return False

        d = {'{': '}', '[': ']', '(': ')'}
        stack = []
        for i in s:
            if i in d:
                stack.append(i)
            else:
                if not stack or d[stack.pop()] != i:
                    return False
        return stack == []