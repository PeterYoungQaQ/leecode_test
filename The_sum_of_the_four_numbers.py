# coding=utf-8 
# @Time :2019/2/2 11:06


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res, dicti = set(), {}
        numLen = len(nums)
        nums.sort()
        for i in range(numLen):
            for j in range(i + 1, numLen):
                key = nums[i] + nums[j]
                if key not in dicti.keys():
                    dicti[key] = [(i, j)]
                else:
                    dicti[key].append((i, j))
        for i in range(numLen):
            for j in range(i + 1, numLen - 2):
                exp = target - nums[i] - nums[j]
                if exp in dicti.keys():
                    for tmpIndex in dicti[exp]:
                        if tmpIndex[0] > j:
                            res.add((nums[i], nums[j], nums[tmpIndex[0]], nums[tmpIndex[1]]))
        return [list(i) for i in res]

