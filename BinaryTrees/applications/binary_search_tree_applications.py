from BinaryTrees.binary_search_tree import Node
from BinaryTrees.binary_search_tree import BinarySearchTree


class BinarySearchTreeApplications(object):
    def __init__(self, root: Node()):
        self.bst_tree = BinarySearchTree(root)

    def tree_includes_recursive(self, root, target):
        if not root:
            return False

        if root.val == target:
            return True

        return self.tree_includes_recursive(root.left, target) \
               | self.tree_includes_recursive(root.right, target)

    def tree_sum_recursive(self, root):
        if not root:
            return 0

        return root.val + self.tree_sum_recursive(root.left) + self.tree_sum_recursive(root.right)

    def min_value_recursive(self, root):
        if not root:
            return float("inf")

        left_min = self.min_value_recursive(root.left)
        right_min = self.min_value_recursive(root.right)

        return min(root.val, left_min, right_min)

    def max_sum_root_leaf_recursive(self, root):
        if not root:
            return float("-inf")

        if not root.left and not root.right:
            return root.val

        left_values = self.max_sum_root_leaf_recursive(root.left)
        right_values = self.max_sum_root_leaf_recursive(root.right)

        return root.val + max(left_values, right_values)

    def invert_tree_recursive(self, root):
        if not root:
            return []

        left_nodes = self.invert_tree_recursive(root.left)
        right_nodes = self.invert_tree_recursive(root.right)

        return [root] + right_nodes + left_nodes

    def tree_height(self, root):
        if not root:
            return 0

        return 1 + max(self.tree_height(root.left), self.tree_height(root.right))

    def tree_size(self, root):
        if not root:
            return 0

        return 1 + self.tree_size(root.left) + self.tree_size(root.right)

    def is_bst_satisfied(self, root):
        if not root:
            return False

        if root.left:
            if root.val <= root.left.val:
                return False
        if root.right:
            if root.val >= root.right.val:
                return False

        self.is_bst_satisfied(root.left)
        self.is_bst_satisfied(root.right)

        return True