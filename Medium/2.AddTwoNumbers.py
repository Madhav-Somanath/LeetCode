""" 
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.

 """
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        out = ListNode(0)
        res = out
        p, q = l1, l2
        carry = 0
        
        while p != None or q != None:
            
            if p != None:
                x = p.val
                p = p.next
            else:
                x = 0
                
            if q != None:
                y = q.val
                q = q.next
            else:
                y = 0
                
            NodeSum = carry + x + y
            carry = NodeSum // 10
            
            res.next = ListNode(NodeSum % 10)
            res = res.next
            
        if carry > 0:
            res.next = ListNode(1)
            
        return out.next