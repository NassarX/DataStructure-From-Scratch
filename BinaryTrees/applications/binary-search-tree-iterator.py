from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.tmp_stack = []

        def helper(root):
            if not root:
                return []

            helper(root.left)
            helper(root.right)
            self.tmp_stack.append(root.val)

        helper(root)
        self.tmp_stack.sort()

    def next(self):
        if len(self.tmp_stack) > 0:
            return self.tmp_stack.pop(0)

    def hasNext(self) -> bool:
        return True if len(self.tmp_stack) > 0 else False


root_node = TreeNode(7)
root_node.left = TreeNode(3)
root_node.right = TreeNode(15)
root_node.right.left = TreeNode(9)
root_node.right.right = TreeNode(20)


# Your BSTIterator object will be instantiated and called as such:
obj = BSTIterator(root_node)
param_1 = obj.next()
param_2 = obj.hasNext()

print(param_1)
print(param_2)
