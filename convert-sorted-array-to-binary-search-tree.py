from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self._sortedArrayToBST(nums,0,len(nums))
    
    def _sortedArrayToBST(self, nums, left, right):
        if left == right:
            return None
        mid = (left + right) >> 1
        root = TreeNode(nums[mid])
        root.left = self._sortedArrayToBST(nums, left, mid)
        root.right = self._sortedArrayToBST(nums, mid + 1, right)
        return root

def see(root:TreeNode):
    print(root.val)
    if root.left:
        see(root.left)
    if root.right:
        see(root.right)

om = Solution().sortedArrayToBST([-10,-3,0,5,9])
see(om)