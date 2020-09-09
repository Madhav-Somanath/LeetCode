""" Implement the StreamChecker class as follows:

    StreamChecker(words): Constructor, init the data structure with the given words.
    query(letter): returns true if and only if for some k >= 1, the last k characters queried (in order from oldest to newest, including this letter just queried) spell one of the words in the given list.
"""

class StreamChecker:

    def __init__(self, words: List[str]):
        self.entries = {}
        for word in words:
            curNode = self.entries           
            for i in range(len(word)):
                cur = word[i]
                if cur not in curNode:
                    curNode[cur] = {}
                curNode = curNode[cur]
            curNode["#"] = True
        self.nodes = []

    def query(self, letter: str) -> bool:
        res = False
        self.nodes.append(self.entries)
        new_nodes = []
        for node in self.nodes:
            if letter in node:
                node = node[letter]
                if "#" in node:
                    res = True
                new_nodes.append(node)
        self.nodes = new_nodes     
        return res
    
'''
    def __init__(self, words):
        T = lambda: collections.defaultdict(T)
        self.trie = T()
        for w in words: reduce(dict.__getitem__, w[::-1], self.trie)['#'] = True
        self.S = ""
        self.W = max(map(len, words))

    def query(self, letter):
        self.S = (letter + self.S)[:self.W]
        cur = self.trie
        for c in self.S:
            if c in cur:
                cur = cur[c]
                if cur['#'] == True:
                    return True
            else:
                break
        return False
        
'''

# There is a difference from 6000ms to 600 ms *_*