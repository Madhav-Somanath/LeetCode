""" Remove all elements from a linked list of integers that have value val. """

# SOLUTION

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        q = ListNode(-1)
        q.next = head
        p = q
        
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        
        return q.next