# coding=utf-8 
# @Time :2019/1/25 15:53


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        left = 0
        right = len(height) - 1
        while right > left:
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return max_area


print(Solution.maxArea(0, [1, 8, 6, 2, 5, 4, 8, 3, 7]))
