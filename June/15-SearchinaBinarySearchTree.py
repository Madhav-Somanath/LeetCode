"""
Given the root node of a binary search tree (BST) and a value.
You need to find the node in the BST that the node's value equals the given value.
Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.
"""

# SOLUTION

def searchBST(self, root: TreeNode, val: int) -> TreeNode:
    
    if not root:
        return None
    if root.val == val:
        return root
    if root.val > val:
        return self.searchBST(root.left, val)
    if root.val< val:
        return self.searchBST(root.right, val)
    
    
# this solution can be iterative too by adding the following:

    # 1. assign a variable "node" to hold root (node = root)
    # 2. same as recursive but you change node to its left or right child (node = node.left/node.right)