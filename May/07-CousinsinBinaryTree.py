'''
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
Return true if and only if the nodes corresponding to the values x and y are cousins.
'''

# SOLUTION

def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
    q = collections.deque()
    ldepth = rdepth = depth = 0
    q.append(root)
    while(q):
        for i in range(len(q)):
            node = q.popleft()
            if node.left and node.right:
                if [node.left.val,node.right.val] == [x,y] or [node.left.val,node.right.val] == [y,x]:
                    return False
            if node.val == x:
                ldepth = depth
            elif node.val == y:
                rdepth = depth
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        depth += 1
    return ldepth == rdepth

# implementation of deque (double ended queue) to keep track of node and a depth parameter running wihtin the while loop.