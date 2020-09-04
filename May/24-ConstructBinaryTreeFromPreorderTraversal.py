"""
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.
"""

# SOLUTION

def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
    
    root = TreeNode(preorder[0])
    stack = [root]
    
    for value in preorder[1:]:
        
        if value < stack[-1].val:
            stack[-1].left = TreeNode(value)
            stack.append(stack[-1].left)
            
        else:
            while stack and stack[-1].val < value:
                last = stack.pop()
                
            last.right = TreeNode(value)
            stack.append(last.right)
            
    return root

'''
        if not preorder: return None
    root = TreeNode(preorder[0])
    i = 1
    while i < len(preorder):
        if preorder[i] < preorder[0]: i += 1
        else: break
    root.left = self.bstFromPreorder(preorder[1:i])
    root.right = self.bstFromPreorder(preorder[i:])
    return root
    
'''