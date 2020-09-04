'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.
Note: Do not use any built-in library function such as sqrt.
'''

# SOLUTION

def isPerfectSquare(num:):
    r = num
    while r*r > num:
        r = (r + num/r) // 2
    return r*r == num

# Basic Newton method application.