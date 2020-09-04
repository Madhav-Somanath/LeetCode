"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

"""

# SOLUTION

def kthSmallest(root, k):
    
    def inorder(r):
        return inorder(r.left) + [r.val] + inorder(r.right) if r else []

    return inorder(root)[k - 1]
    
# sonvert the tree into inorder form and return (k-1)th element.