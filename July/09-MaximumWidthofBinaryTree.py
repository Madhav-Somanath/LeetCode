""" Given a binary tree, write a function to get the maximum width of the given tree. 
The width of a tree is the maximum width among all levels. 
The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes 
the leftmost and right most non-null nodes in the level, where the null nodes between
the end-nodes are also counted into the length calculation. """

# SOLUTION

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        width = 0
        level = [(1, root)]
        while level:
            width = max(width, level[-1][0] - level[0][0] + 1)
            level = [kid for number, node in level 
                     for kid in enumerate((node.left, node.right), 2 * number) if kid[1]]
        return width
    
'''
If we go down the left neighbor, then position -> position * 2; and if we go down the right neighbor,
then position -> position * 2 + 1. This makes it so that when we look at the position values L and R of two nodes with the same depth,
the width will be R - L + 1.
'''