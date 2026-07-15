# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max = 0

        def depth(root):
            if not root:
                return 0

            self.max = max(self.max, depth(root.left) +depth(root.right))
            return 1 + max(depth(root.left), depth(root.right))

        depth(root)

        return self.max