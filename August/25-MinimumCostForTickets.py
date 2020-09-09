""" In a country popular for train travel, you have planned some train travelling one year in advance.  The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

Train tickets are sold in 3 different ways:

    a 1-day pass is sold for costs[0] dollars;
    a 7-day pass is sold for costs[1] dollars;
    a 30-day pass is sold for costs[2] dollars.

The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days. """

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        # Create dictionary for faster lookup of days
        import collections
        days_dict = collections.Counter(days)
        
        # Create a table of all the day cost
        # * Instead of creating a 365 days table, we create until the last day on the days list
        
        table = [0 for i in range(0, days[-1]+1)]
        
        for i in range(0, days[-1]+1):
            
            # If the current day is not present in the travel days dictionary, it takes the previous value
            if i not in days_dict:
                table[i] = table[i-1]
                
            else:
                # Used max to identify if the index exists 
                table[i] = min(
                    table[max(0,i-1)]+costs[0], # per days value
                    table[max(0,i-7)]+costs[1], # per week value
                    table[max(0,i-30)]+costs[2] # per year value
                )
        
        return table[-1]
    
# Complexity analysis:
#   Time Complexity: O(N), where N is the number of calendar days.
#   Space Complexity: O(N)
