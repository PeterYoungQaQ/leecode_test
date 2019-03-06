# coding=utf-8
# @Time: 3/6/2019 5:36 PM
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):  # 遍历数组
            if nums[i] != 0:
                continue  # 如果不为0，就进行下一次循环
            else:  # 找到了第i个数是0
                temp = nums[0:i + 1][::-1]
                count = 0
                flag = False
                for item in temp:
                    if item > count:
                        flag = True  # 可以跳到该位置
                        break
                    count += 1
                if not flag: return False
        return True


print(Solution().canJump([2, 3, 1, 1, 4]))
