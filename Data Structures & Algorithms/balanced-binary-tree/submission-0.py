# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def getDepth(root):
            if not root:
                return 0

            left = 1 + getDepth(root.left)
            right = 1 + getDepth(root.right)

            if abs(left - right) > 1:
                self.balanced = False

            return max(left, right)

        getDepth(root)
        return self.balanced

         
