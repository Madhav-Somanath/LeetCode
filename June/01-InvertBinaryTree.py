"""
Do i need to explain this question?
"""

# SOLUTION

# recursive
def invertTree(self, root):
    if root:
        invert = self.invertTree
        root.left, root.right = invert(root.right), invert(root.left)
        return root

# iterative
def invertTree(self, root):
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left
            stack += node.left, node.right
    return root

# Classical tree problem: inspiration -> https://twitter.com/mxcl/status/608682016205344768