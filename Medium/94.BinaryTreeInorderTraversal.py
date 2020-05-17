"""
Given a binary tree, return the inorder traversal of its nodes' values.
"""

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        res = []
        self.helper(root, res)
        
        return res
    
    def helper(self, root, res):
        if root:
            if root.left:
                self.helper(root.left, res)
                
            res.append(root.val)
            
            if root.right:
                self.helper(root.right, res)