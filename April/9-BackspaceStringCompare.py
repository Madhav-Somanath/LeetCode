def backspaceCompare(S, T):
    s1 = []
    s2 = []
    
    for val in S:
        if val == '#':
            if s1:
                s1.pop()
        else:
            s1.append(val)
    
    for val in T:
        if val == '#':
            if s2:
                s2.pop()
        else:
            s2.append(val)
    
    return s1 == s2