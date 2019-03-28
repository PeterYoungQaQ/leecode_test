# coding=utf-8 
# @Time :2019/3/28 15:22

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.validBST(root, -2 ** 32, 2 ** 32 - 1)

    def validBST(self, root, small, large):
        if root is None:
            return True
        if small >= root.val or large <= root.val:
            return False
        return self.validBST(root.left, small, root.val) and self.validBST(root.right, root.val, large)


print(Solution().isValidBST([2, 1, 3]))
