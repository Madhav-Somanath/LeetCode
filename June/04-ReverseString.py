"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.
"""

# SOLUTION

def reverseString(s: List[str]) -> None:
    """
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left, right = left + 1, right - 1
    """
    
    # BUT WHY DO WE NEED TWO POINTERS?
    
    for i in range(len(s)//2):
        s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]
        
# Simple and elegant solution, simply using reverse() calls in a recursion stack which means its not O(1).
