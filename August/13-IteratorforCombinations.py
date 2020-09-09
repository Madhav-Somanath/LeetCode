""" Design an Iterator class, which has:

    A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
    A function next() that returns the next combination of length combinationLength in lexicographical order.
    A function hasNext() that returns True if and only if there exists a next combination.
"""

from itertools import combinations
class CombinationIterator:

    def __init__(self, characters, combinationLength):
        self.it = combinations(characters, combinationLength)
        self.buffer = next(self.it, None)
        
    def next(self):
        res = ''.join(self.buffer)
        self.buffer = next(self.it, None)
        return res
        
    def hasNext(self):
        return self.buffer is not None

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()

'''
    def __init__(self, characters, length):
        self.generator = self.gen(characters, length)
        self.buffer = next(self.generator)
        
    def gen(self, characters, length):
        if length == 0:
            yield ""
        elif len(characters) == length:
            yield characters
        elif len(characters) > length:
            for tail in self.gen(characters[1:], length - 1):
                yield characters[0] + tail
            for tail in self.gen(characters[1:], length):
                yield tail
        
    def next(self):
        res = self.buffer
        try:
            self.buffer = next(self.generator)
        except StopIteration:
            self.buffer = None
        return res
        
    def hasNext(self):
        return self.buffer is not None
'''