# coding=utf-8
# @Time: 3/25/2019 4:36 PM


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0: return []
        return self.generateTreesDFS(1, n)

    def generateTreesDFS(self, left, right):
        if left > right:
            return [None]
        res = []
        for i in range(left, right + 1):
            left_nodes = self.generateTreesDFS(left, i - 1)
            right_nodes = self.generateTreesDFS(i + 1, right)
            for left_node in left_nodes:
                for right_node in right_nodes:
                    root = TreeNode(i)
                    root.left = left_node
                    root.right = right_node
                    res.append(root)
        return res


print(Solution().generateTrees(3))
