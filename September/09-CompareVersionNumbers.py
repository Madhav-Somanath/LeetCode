""" Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.

The . character does not represent a decimal point and is used to separate number sequences.

For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

You may assume the default revision number for each level of a version number to be 0. For example, version number 3.4 has a revision number of 3 and 4 for its first and second level revision number.
Its third and fourth level revision number are both 0. """

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        s1 = [int(i) for i in version1.split(".")]
        s2 = [int(i) for i in version2.split(".")]
        
        l1, l2 = len(s1), len(s2)
        
        if l1 < l2:
            s1 += [0]*(l2 - l1) 
        else:
            s2 += [0]*(l1 - l2)
            
        return (s1 > s2) - (s1 < s2)
            
            