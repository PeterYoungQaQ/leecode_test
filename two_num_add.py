# coding=utf-8

"""
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


# 利用双指针的方式
def sol1(self, nums, target):
    nums_bak = nums.copy()
    nums.sort()
    i = 0
    j = 0
    for k in range(0, (len(nums) - 1)):
        if nums[k] + nums[k + 1] >= target:
            i = k
            j = k + 1
            break
    while i >= 0 and j < len(nums):
        if nums[i] + nums[j] < target:
            j += 1
        elif nums[i] + nums[j] > target:
            i -= 1
        else:
            if nums[i] == nums[j]:
                return [nums_bak.index(nums[i]), nums_bak.index(nums[j], i + 1)]
            else:
                return [nums_bak.index(nums[i]), nums_bak.index(nums[j])]


# 利用哈希表,主要是利用枚举enumerate的功能
def sol2(self, nums, target):
    result = []
    for i, value in enumerate(nums):
        if (target - value) in nums[i + 1:]:
            result.append((value, target - value))
    return result
