# coding=utf-8
# @Time: 3/29/2019 1:49 PM

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def f(p, q):
            if p is None:
                return q is None
            if q is None:
                return p is None
            if p.val == q.val:
                return f(p.left, q.right) and f(p.right, q.left)
            if p.val != q.val:
                return False

        if root is None:
            return True
        return f(root.left, root.right)



