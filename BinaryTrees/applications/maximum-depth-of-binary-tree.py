# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root) -> int:
        return (1 + max(self.maxDepth(root.left), self.maxDepth(root.right))) if root else 0

solution = Solution()
root_node = TreeNode(7)
root_node.left = TreeNode(3)
root_node.right = TreeNode(15)
root_node.right.left = TreeNode(9)
root_node.right.right = TreeNode(20)

print(solution.maxDepth(root_node))
