# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root_store = root

        queue = deque()
        queue.append(root)
        i = 0

        while i < len(queue):
            node = queue[i]

            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)

            temp = node.left

            node.left = node.right
            node.right = temp

            i += 1

        return root_store



