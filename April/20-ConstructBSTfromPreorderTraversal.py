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