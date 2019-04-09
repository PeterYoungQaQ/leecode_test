# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.height(root) != -1
    def height(self, node):
            if not node:
                return 0
            left = self.height(node.left)
            right = self.height(node.right)
            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1

            return max(left,right) + 1
        