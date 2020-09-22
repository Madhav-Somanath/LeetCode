""" Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space. """

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter()
        
        for num in nums:
            count[num] += 1
            
            if len(count) == 3:
                for elem, freq in count.items():
                    count[elem] -= 1
                    
        cands = Counter(num for num in nums if num in count)  
        
        return [num for num in cands if cands[num] > len(nums)/3]
    
    '''Time complexity is O(n), because we traverse our nums twice: on first run we process each number at most twice: when we add it to counter and when remove. Second run, where we evaluate frequencies of candidates is also linear. Space complexity is O("k"),
    because our counter always have no more than 3 elements.(probably)'''