def middleNode(head):
    
    if not head:
        return None
    
    fast = slow = head
    
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        
    return slow
        