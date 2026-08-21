# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0
        def helper(curr):
            if not curr:
                return 0
            leftHeight = helper(curr.left)
            rightHeight = helper(curr.right)
            height = max(leftHeight, rightHeight) + 1
            nonlocal maxDiameter
            maxDiameter = max(leftHeight + rightHeight, maxDiameter)
            return height
        helper(root)
        return maxDiameter