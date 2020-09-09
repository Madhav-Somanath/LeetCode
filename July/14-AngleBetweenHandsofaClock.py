""" Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand. """

# SOLUTION

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:

        h = (hour%12 * 30) + (minutes/60 * 30)
        m = minutes * 6
        angle = abs(m - h)
        if angle > 180:
            angle = 360.0 - angle
            
        return (angle)
    
# straightforward math solution 