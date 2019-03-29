# coding=utf-8
# @Time: 3/29/2019 3:57 PM

# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if not root:
            return result
        curr_level = [root]
        need_reverse = False
        while curr_level:
            level_result = []
            next_level = []
            for temp in curr_level:
                level_result.append(temp.val)
                if temp.left:
                    next_level.append(temp.left)
                if temp.right:
                    next_level.append(temp.right)
            if need_reverse:
                level_result.reverse()
                need_reverse = False
            else:
                need_reverse = True
            result.append(level_result)
            curr_level = next_level
        return result