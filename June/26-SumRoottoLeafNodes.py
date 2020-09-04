"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.
"""

# SOLUTION

def sumNumbers(root: TreeNode) -> int:
    if not root:
        return 0
    stack, res = [(root, root.val)], 0
    while stack:
        node, value = stack.pop()
        if node:
            if not node.left and not node.right:
                res += value
            if node.right:
                stack.append((node.right, value*10+node.right.val))
            if node.left:
                stack.append((node.left, value*10+node.left.val))
    return res

'''
# bfs + queue
def sumNumbers2(root):
    if not root:
        return 0
    queue, res = collections.deque([(root, root.val)]), 0
    while queue:
        node, value = queue.popleft()
        if node:
            if not node.left and not node.right:
                res += value
            if node.left:
                queue.append((node.left, value*10+node.left.val))
            if node.right:
                queue.append((node.right, value*10+node.right.val))
    return res

# recursively 
def sumNumbers(root):
    self.res = 0
    self.dfs(root, 0)
    return self.res
    
def dfs(root, value):
    if root:
        #if not root.left and not root.right:
        #    self.res += value*10 + root.val
        self.dfs(root.left, value*10+root.val)
        #if not root.left and not root.right:
        #    self.res += value*10 + root.val
        self.dfs(root.right, value*10+root.val)
        if not root.left and not root.right:
            self.res += value*10 + root.val
'''