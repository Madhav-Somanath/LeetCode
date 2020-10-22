""" Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children. """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        res, stack = float('inf'), [(root, 1)]
        
        while stack:
            node, level = stack.pop()
            if node and not node.left and not node.right:
                res = min(res, level)
            if node:
                stack.append((node.left, level+1))
                stack.append((node.right, level+1))
        return res
    
    '''
    # Recursive
    
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    if root.left and not root.right:
        return 1 + self.minDepth(root.left)
    if root.right and not root.left:
        return 1 + self.minDepth(root.right)
    return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
    '''