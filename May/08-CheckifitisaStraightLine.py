'''
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. 
Check if these points make a straight line in the XY plane.
'''

# SOLUTION

def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
    
    (x0, y0), (x1, y1) = coordinates[: 2]
    return all((x1 - x0) * (y - y1) == (x - x1) * (y1 - y0) for x, y in coordinates)

# Basic math with good use of "any" within python, utilization of for loop within python.