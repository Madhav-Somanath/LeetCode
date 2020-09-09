""" Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)

search(word) can search a literal word or a regular expression string containing only letters a-z or .
A . means it can represent any one letter. """]

from collections import defaultdict

class WordDictionary:

    def __init__(self):

        Trie = lambda: defaultdict(Trie)
        self.root = Trie()

    def addWord(self, word: str) -> None:

        node = self.root
        for letter in word:
            node = node[letter]
        node['$'] = True

    def search(self, word: str) -> bool:

        def helper(word, i, node):
            if i == len(word):
                return '$' in node
            elif word[i] == '.':
                return any(
                    helper(word, i+1, node[letter])
                    for letter in node
                    if letter != '$'
                )
            elif word[i] in node:
                return helper(word, i+1, node[word[i]])
            else:
                return False
        return helper(word, 0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)