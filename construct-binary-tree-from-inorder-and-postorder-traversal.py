from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        self.postorder = postorder
        self.inorder = inorder
        return self._buildTree(0, len(inorder))

    def _buildTree(self, start, end):
        if start < end:
            root = TreeNode(self.postorder.pop())
            index = self.inorder.index(root.val)
            root.right = self._buildTree(index + 1, end)
            root.left = self._buildTree(start, index)
            return root