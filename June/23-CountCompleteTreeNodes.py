"""
Given a complete binary tree, count the number of nodes.
"""

# SOLUTION

def countNodes(root: TreeNode) -> int:
    if not root:
        return 0
    
    leftDepth = getDepth(root.left)
    rightDepth = getDepth(root.right)
    
    if leftDepth == rightDepth:
        return pow(2, leftDepth) + countNodes(root.right)
    else:
        return pow(2, rightDepth) + countNodes(root.left)

def getDepth(root):
    if not root:
        return 0
    return 1 + getDepth(root.left)