# coding=utf-8
# @Time: 3/11/2019 1:32 PM


class Solution:
    def isNumber0(self, s: str) -> bool:
        try:
            b = float(s)
            print(b)
            return True
        except:
            return False

    # 这个办法有问题，不能解决“"1 "为True的问题
    def isNumber1(self, s: str) -> bool:
        num, dot, exp, sign = False, False, False, False
        numAfterE = True
        n = len(s)
        for i in range(n):
            # 当前位置是空格而后面一位不为空格，但是之前有数字，小数点，自然底数或者符号出现时返回false。
            if s[i] == '':
                if i < n - 1 and s[i + 1] != ' ' and (num or dot or exp or sign):
                    return False
            # 符号前面如果有字符的话必须是空格或者是自然底数，标记sign为true
            elif s[i] == '+' or s[i] == '-':
                if i > 0 and s[i - 1] != 'e' and s[i - 1] != ' ':
                    return False
                sign = True
            # 如果是数字出现，标记num和numAfterE为true
            elif '0' <= s[i] <= '9':
                num = True
                numAfterE = True
            # 小数点：如果之前出现过小数点或者自然底数，返回false，否则标记dot为true
            elif s[i] == '.':
                if dot or exp:
                    return False
                dot = True
            # 自然底数：如果之前出现过自然底数或者之前从未出现过数字，返回false，否则标记exp为true，numAfterE为false。
            elif s[i] == 'e':
                if exp or (not num):
                    return False
                exp = True
                numAfterE = False
            else:
                return False

        return num and numAfterE

    def isNumber2(self, s: str) -> bool:
        def isInt(s):
            NO_NUM = True
            for i in range(len(s)):
                # 正负号只能在首位
                if s[i] == "+" or s[i] == '-':
                    if i == 0:
                        continue
                    else:
                        return False
                # 至少有一个数字
                elif s[i] in "1234567890":
                    NO_NUM = False
                # 不能有其他字符
                else:
                    return False

            return not NO_NUM

        def isFloat(s):
            DOT_COUNT = 0
            NO_NUM = True
            for i in range(len(s)):
                # 正负号只能在首位
                if s[i] == "+" or s[i] == "-":
                    if i == 0:
                        continue
                    else:
                        return False
                # 小数点至多有一个
                elif s[i] == '.':
                    DOT_COUNT += 1
                    if DOT_COUNT > 1:
                        return False
                # 至少有一个数字
                    elif s[i] in "1234567890":
                        NO_NUM = False
                    # 不能有其他字符
                    else:
                        return False

            return not NO_NUM

        s =s.strip()
        if 'e' not in s:
            return isFloat(s)
        else:
            t = s.split('e')
            if len(t) == 2:
                return isInt(t[1]) and isFloat(t[0])
            else:
                return False


print(Solution().isNumber2("1 "))