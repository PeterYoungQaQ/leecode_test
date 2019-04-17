
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res= []
        self.pathSum_solve(root, sum, res, [root.val])
        return res
    
    def pathSum_solve(self, root, target, res, path):
        if not root:
            return
        if sum(path) == target and not root.left and not root.right:
            res.append(path)
            return
        if root.left:
            self.pathSum_solve(root.left, target, res, path + [root.left.val])
        if root.right:
            self.pathSum_solve(root.right, target, res, path + [root.right.val])
