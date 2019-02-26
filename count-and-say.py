# coding=utf-8
# @Time: 2/26/2019 2:16 PM

class Solution:
    def countAndSay(self, n: int) -> str:
        res = ["1"]
        for i in range(n):
            num = res[i]
            temp = num[0]  # 当前的数值
            count = 0
            ans = ""
            for j in range(0, len(num)):
                if num[j] == temp:
                    count += 1
                else:
                    ans += str(count)
                    ans += str(temp)
                    temp = num[j]
                    count = 1
            ans += str(count)
            ans += str(temp)
            res.append(ans)
        return res[n - 1]


print(Solution().countAndSay(4))
