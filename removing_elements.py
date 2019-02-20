
# coding=utf-8 
# @Time :2019/2/20 10:27

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.pop(nums.index(val))
        return len(nums), nums

print(Solution.removeElement(0, [1,2,3,2,5,3], 2))
