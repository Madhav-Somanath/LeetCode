def stringShift(self, s: str, shift: List[List[int]]) -> str:
    tshift = 0
    
    for sh in shift:
        if sh[0] == 0:
            tshift -= sh[1]
        else:
            tshift += sh[1]
    
    tshift %= len(s)

    return s[-tshift:]+s[:-tshift]