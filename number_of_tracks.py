# coding=utf-8 
# @Time :2019/1/25 14:40


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a = str(x)
        l = len(a)
        flag = True
        for i in range(0, l // 2):
            if a[i] != a[-i-1]:
                flag = False
                break
        if flag:
            return True
        else:
            return False





print(Solution.isPalindrome(0, 10))




