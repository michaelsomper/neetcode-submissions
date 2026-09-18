# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.same = True
        
        def compare(p, q) -> bool:
            if not p and not q:
                return None

            if q and not p:
                self.same = False
                return None

            if p and not q:
                self.same = False
                return None

            if p.val != q.val:
                self.same = False

            compare(p.left, q.left)
            compare(p.right, q.right)

        compare(p, q)

        return self.same
