def diameterOfBinaryTree(root):
    ans = 0
    
    def depth(p):
        if not p: return 0
        left, right = depth(p.left), depth(p.right)
        ans = max(ans, left+right)
        return 1 + max(left, right)
        
    depth(root)
    return ans