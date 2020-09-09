""" You are given a char array representing tasks CPU need to do.
It contains capital letters A to Z where each letter represents a different task.
Tasks could be done without the original order of the array. Each task is done in one unit of time.
For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array),
that is that there must be at least n units of time between any two same tasks.

You need to return the least number of units of times that the CPU will take to finish all the given tasks. """

# SOLUTION

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_count = list(collections.Counter(tasks).values())
        max_count = max(tasks_count)
        max_count_tasks = tasks_count.count(max_count)
        return max(len(tasks), (max_count-1)*(n+1)+max_count_tasks)
    
    '''
    curr_time, h = 0, []
    for k,v in Counter(tasks).items():
        heappush(h, (-1*v, k))
    while h:
        i, temp = 0, []
        while i <= n:
            curr_time += 1
            if h:
                x,y = heappop(h)
                if x != -1:
                    temp.append((x+1,y))
            if not h and not temp:
                break
            else:
                i += 1
        for item in temp:
            heappush(h, item)
    return curr_time
    -------------------------------------
        n = len(tasks)
        freq = [0] * 26
        
        for i in range(n):
            freq[self.cnum(tasks[i])] += 1
        freq.sort()
        maxfreq = freq[25]
        maxcount = freq.count(maxfreq)
                
        slots = (maxfreq-1) * k
        occupied = (maxcount-1) * (maxfreq-1)
        occupied += (n-maxcount*maxfreq)
        slots = max(0, slots-occupied) 
        
        return n + slots
        
    def cnum(self, char):
        return ord(char) - ord('A')
        
    '''