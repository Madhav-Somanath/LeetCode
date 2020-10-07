""" Given a linked list, rotate the list to the right by k places, where k is non-negative. """

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        pointer = head
        count = 1
        while pointer.next:
            count+=1
            pointer = pointer.next
        
        n = k % count
        if n == 0:
            return head
        slow = fast = head
        for _ in range(n):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next, fast.next, head =None, head, slow.next
        return head
    
    '''
    if not head or not k:
        return head      # special cases
        
    tail = cur = head
    n = 0
    while cur and cur.next:                # get size of linked list
        cur = cur.next
        n += 1
        
    tail = cur                             # get the tail
    n += 1                                 # adjust the size
    k = k % n                              # take mod of k in case k > n
    
    if not k:
        return head                        # if k is zero, no rotation
    n = n-k-1                              # locate new head node
    cur = head        
    
    for _ in range(n):
        cur = cur.next
        
    new_head = cur.next                    # get the new head
    cur.next = None                        # delink tail
    tail.next = head                       # connect tail to original head
    
    return new_head
    '''