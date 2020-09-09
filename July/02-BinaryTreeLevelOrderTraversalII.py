""" Given a binary tree, return the bottom-up level order traversal of its nodes values.
(ie, from left to right, level by level from leaf to root). """

# SOLUTION

def levelOrderBottom(root: TreeNode) -> List[List[int]]:
    res = []
    dfs(root, 0, res)
    return res

def dfs(self, root, level, res):
    if root:
        if len(res) < level + 1:
            res.insert(0, [])
        res[-(level+1)].append(root.val)
        dfs(root.left, level+1, res)
        dfs(root.right, level+1, res)
        
'''
stack = [(root, 0)]
res = []
while stack:
    node, level = stack.pop()
    if node:
        if len(res) < level+1:
            res.insert(0, [])
        res[-(level+1)].append(node.val)
        stack.append((node.right, level+1))
        stack.append((node.left, level+1))
return res
'''