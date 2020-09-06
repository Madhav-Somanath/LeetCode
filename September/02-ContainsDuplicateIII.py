""" Given an array of integers,find out whether there are two distinct indices i and j in the array such that 
the absolute difference between nums[i] and nums[j]is at most t and the absolute difference between i and j is at most k. """

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        
        if k < 1 or t < 0:
            return False
        
        dic = collections.OrderedDict()
        
        for n in nums:
            key = n if not t else n // t
            
            for m in (dic.get(key - 1), dic.get(key), dic.get(key + 1)):
                if m is not None and abs(n - m) <= t:
                    return True
                
            if len(dic) == k:
                dic.popitem(False)
                
            dic[key] = n
            
        return False