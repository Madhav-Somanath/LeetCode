""" Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents
a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1,
then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers. """

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        
        def dfs(node):
            if not node.left and not node.right: self.sum += node.val
            for child in filter(None, [node.left, node.right]):
                child.val += node.val * 2
                dfs(child)
                
        self.sum = 0
        dfs(root)
        return self.sum
    
'''
# without changinf tree
def dfs(node, Q):
        if not node.left and not node.right: self.sum += Q
        for child in filter(None, [node.left, node.right]):
            dfs(child, Q*2 + child.val)

    self.sum = 0
    dfs(root, root.val)
    return self.sum
'''

# O(N) time O(H) space