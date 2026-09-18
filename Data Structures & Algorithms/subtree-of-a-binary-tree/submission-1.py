class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same(p, q) -> bool:
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return is_same(p.left, q.left) and is_same(p.right, q.right)

        def find(node) -> bool:
            if not node:
                return False

            # If this node matches, we're done
            if is_same(node, subRoot):
                return True

            # Otherwise, keep searching both branches
            return find(node.left) or find(node.right)

        return find(root)