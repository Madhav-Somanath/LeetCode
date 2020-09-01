def isValidSequence(root, arr):
    l = len(arr)
    i = 0
    return check(root, arr, l, i)

def check(root, arr, l, i):
    if root is None:
        return l == 0
    
    if (i == l-1) and (root.left == None and root.right == None) and (root.val == arr[i]):
        return True
    
    if (i<l) and (root.val == arr[i]):
        return check(root.left, arr, l, i+1) or check(root.right, arr, l, i+1)