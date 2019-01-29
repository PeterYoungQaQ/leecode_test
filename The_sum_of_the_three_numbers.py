# coding=utf-8 
# @Time :2019/1/29 14:26


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i == 0 or nums[i] > nums[i - 1]:
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    ident = nums[left] + nums[right] + nums[i]
                    if ident == 0:
                        ans.append([nums[i], nums[left], nums[right]])
                        left += 1;
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:  # skip duplicates
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif ident < 0:
                        left += 1
                    else:
                        right -= 1
        return ans


class Solution1:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 记录最小的差值,先给出一个较大的数进行比较，否则无法存储每次求得的差值
        minDiff = 10000
        # 记录最小差值对应的三个整数和
        result = 0
        # 每次求得的差值
        diff = 0
        # 每次求得的三个整数的和
        sum = 0

        # 先对数组进行排序，无返回值，排序后改变nums数组顺序
        nums.sort()

        # i表示假设取第i个数作为结果
        for i in range(len(nums) - 2):
            # 第二个数的起始位置
            j = i + 1
            # 第三个数是结束位置
            k = len(nums) - 1

            while j < k:
                # 求当前三个数的和
                sum = nums[j] + nums[k] + nums[i]
                # 当前和与目标和之间的差值
                diff = abs(target - sum)

                # 差值为0就直接返回
                if diff == 0:
                    return sum

                # 如果当前的差值比之前记录的差值小，则存储当前小的差值进minDiff，接近的结果和存储进result
                if diff < minDiff:
                    # 更新最小的差值
                    minDiff = diff
                    # 更新最小差值对应的和
                    result = sum
                    # 以上的设置在下一次元素处理时生效

                # 和大于target
                if sum > target:
                    k -= 1
                # 和小于target
                else:
                    j += 1

        return result

