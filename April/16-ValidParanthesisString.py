def checkValidString(self, s: str) -> bool:
    if not s:
        return True

    left = list()
    star = list()
    
    for i, c in enumerate(s):
        if c == "*":
            star.append(i)
        elif c == "(":
            left.append(i)
        elif c == ")":
            if left:
                left.pop()
            elif star:
                star.pop()
            else:
                return False
    
    if len(left) > len(star):
        return False
    
    while left and star:
        if left.pop() > star.pop():
            return False
    
    return True