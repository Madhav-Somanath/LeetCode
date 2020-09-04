"""
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
"""

# SOLUTION

def deleteNode(self, node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    node.val = node.next.val
    node.next = node.next.next