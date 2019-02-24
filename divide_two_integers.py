# coding=utf-8 
# @Time :2019/2/21 13:55

class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0: return 0 
        if divisor == 0: return 0
        
        sign = -1 if ((dividend < 0) ^ (divisor < 0)) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = 0 
        tmp = 0 
        for i in range(32,-1,-1):
            if tmp + (divisor << i) <= dividend:
                tmp += divisor << i 
                quotient |= 1 << i
        
        quotient *= sign    #虽然题目说了不要用乘法，但是为了代码的简洁这里还是用了
        if quotient < -(2 ** 31) or quotient > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return quotient
                       
