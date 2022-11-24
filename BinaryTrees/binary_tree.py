class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = root

    @staticmethod
    def reverse_breadth_first_values_iterative(root):
        if not root:
            return []

        values_stack = []
        tmp_queue = [root]

        while len(tmp_queue) > 0:
            current = tmp_queue.pop(0)
            values_stack.append(current)

            if current.right:
                tmp_queue.append(current.right)

            if current.left:
                tmp_queue.append(current.left)

        values_stack.reverse()
        return values_stack

    @staticmethod
    def breadth_first_values_iterative(root):
        if not root:
            return []

        tmp_queue = [root]
        values = []

        while len(tmp_queue) > 0:
            current_node = tmp_queue.pop(0)
            values.append(current_node)
            if current_node.left:
                tmp_queue.append(current_node.left)

            if current_node.right:
                tmp_queue.append(current_node.right)

        return values

    @staticmethod
    def depth_first_values_iterative(root):
        if not root:
            return []

        tmp_stack = [root]
        values = []

        while len(tmp_stack) > 0:
            current_node = tmp_stack.pop()
            values.append(current_node)
            if current_node.right:
                tmp_stack.append(current_node.right)

            if current_node.left:
                tmp_stack.append(current_node.left)

        return values

    def depth_first_values_recursive(self, root):
        if not root:
            return []

        left_values = self.depth_first_values_recursive(root.left)
        right_values = self.depth_first_values_recursive(root.right)

        return [root] + left_values + right_values

    @staticmethod
    def tree_includes(root, target) -> bool:
        if not root:
            return False

        tmp_queue = [root]
        while len(tmp_queue) > 0:
            current_node = tmp_queue.pop(0)
            if current_node.val == target:
                return True
            if current_node.left:
                tmp_queue.append(current_node.left)

            if current_node.right:
                tmp_queue.append(current_node.right)

        return False

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




a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f


tree = BinaryTree(a)
print(tree.tree_size(a))

# r = tree.depth_first_values(a)
# r = tree.reverse_breadth_first_values_iterative(a)
r = tree.depth_first_values_recursive(a)
# print(tree.lefts)
print([x.val for x in r])

#rr = tree.tree_includes(a, "H")
rr = tree.tree_includes_recursive(a, "A")

rrr = tree.invert_tree_recursive(a)

print(print([x.val for x in rrr]))




a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
_sum = tree.tree_sum_recursive(a)
_sum = tree.min_value_recursive(a)
_sum = tree.max_sum_root_leaf_recursive(a)
print(_sum)

print(tree.tree_height(a))
print(tree.tree_size(a))
