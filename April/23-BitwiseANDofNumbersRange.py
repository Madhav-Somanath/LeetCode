def rangeBitwiseAnd(m, n):
    p = 0
    while m != n:
        m >>= 1
        n >>= 1
        p += 1
    return m << p
    