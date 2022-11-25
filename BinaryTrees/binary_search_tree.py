class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree(object):
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

        return left_values + [root.val] + right_values

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

    def insert_helper(self, root, node):
        if node.val > root.val:
            if root.right:
                self.insert_helper(root.right, node)
            else:
                root.right = node
        else:
            if root.left:
                self.insert_helper(root.left, node)
            else:
                root.left = node

    def insert(self, node: Node()):
        self.insert_helper(self.root, node)


# Set up tree:
a = Node(1)
tree = BinarySearchTree(a)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.depth_first_values_recursive(a))