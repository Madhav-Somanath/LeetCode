def maxPathSum(root):
    self.ans = -sys.maxsize if root else 0
    
    def walk(node):
        
        if not node:
            return 0
        
        lsum, rsum = walk(node.left), walk(node.right)
        if lsum < 0 and rsum < 0:
            self.ans = max(self.ans, node.val)
            return node.val
        elif lsum >= 0 and rsum < 0:
            self.ans = max(self.ans, node.val + lsum)
            return node.val + lsum
        elif lsum < 0 and rsum >= 0:
            self.ans = max(self.ans, node.val + rsum)
            return node.val + rsum
        else: 
            self.ans = max(self.ans, node.val + lsum + rsum)
            return node.val + max(lsum, rsum)
        
    walk(root)
    return self.ans