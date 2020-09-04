'''
Given a non-negative integer num represented as a string,
remove k digits from the number so that the new number is the smallest possible.

Note:
    The length of num is less than 10002 and will be ≥ k.
    The given num does not contain any leading zero.

'''

# SOLUTION

def removeKdigits(num, k):
    if len(num) <= k:
        return '0'
    
    stack = []
    
    for digit in num:
        while k> 0 and stack and int(stack[-1]) > int(digit): 
            stack.pop()
            k -= 1
        stack.append(digit)
    
    while k > 0: #corner case 112 remove 1
        stack.pop()
        k -= 1
    return ''.join(stack).lstrip('0') or '0'

# I think this process is technically called monotonic queue