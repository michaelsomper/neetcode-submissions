class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack = [root]
        parent = {root: None}

        # 1. Traverse until both p and q are found in parent
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # 2. Collect all ancestors of p into a set
        ancestors_p = set()
        curr = p
        while curr:
            ancestors_p.add(curr)
            curr = parent[curr]

        # 3. Walk q up; the first ancestor of q in ancestors_p is the LCA
        curr = q
        while curr not in ancestors_p:
            curr = parent[curr]

        return curr