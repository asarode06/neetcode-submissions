# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        balanced = True
        def calcHeight(node):
            nonlocal balanced
            lHeight = -1
            rHeight = -1
            if node.left:
                lHeight = calcHeight(node.left)
            if node.right:
                rHeight = calcHeight(node.right)
            print(node.val, lHeight, rHeight)
            if abs(lHeight - rHeight) > 1:
                balanced = False
            return max(lHeight, rHeight) + 1
        calcHeight(root)
        return balanced