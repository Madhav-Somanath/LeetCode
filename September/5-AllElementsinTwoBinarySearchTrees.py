""" Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order. """

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(node: TreeNode) -> None:
            if not node:
                return
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)
        ans = []
        inorder(root1)
        inorder(root2)
        return sorted(ans)