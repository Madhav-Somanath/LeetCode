"""
Given a singly linked list, group all odd nodes together followed by the even nodes.
Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
"""

# SOLUTION

def oddEvenList(head):
    
    if head is None:
        return None
    
    odd = head
    even = head.next
    evenhead = even
    
    while even != None and even.next != None:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    
    odd.next = evenhead
    
    return head

# no real extra solution here straightforward thinking.