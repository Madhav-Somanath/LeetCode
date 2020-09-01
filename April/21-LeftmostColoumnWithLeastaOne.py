def leftMostColumnWithOne(self, binaryMatrix):
    r, c = binaryMatrix.dimensions()
    i = r-1
    j= c-1
    while i>=0 and j>=0:
        if binaryMatrix.get(i,j) == 0:
            i-=1
        else:
            j-=1
        
    return -1 if j == c-1  else j+1
