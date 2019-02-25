# coding=utf-8
# @Time: 2/25/2019 2:27 PM

class Solution:
    def searchInsert(self, nums: 'List[int]', target: 'int') -> 'int':
        if target in nums:
            return nums.index(target)
        else:
            count = 0
            for i in nums:
                if i > target:
                    return count
                count += 1
            return len(nums)
