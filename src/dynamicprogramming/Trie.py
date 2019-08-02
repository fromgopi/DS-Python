from collections import defaultdict
from pprint import pprint as pp


class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word):
        trie = self.trie
        for char in word:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
        trie['*'] = True

    def elements(self, prefix):
        trie = self.trie
        for char in prefix:
            if char in trie:
                trie = trie[char]
            else:
                return []
        return self._element(trie)

    def _element(self, b):
        results = []
        for s, v in b.items():
            if s == '*':
                subresult = ['']
            else:
                subresult = [s + k for k in self._element(v)]
            results.append(subresult[0])
        return results


def match_prefix(trie, s):
    suffixes = trie.elements(s)
    return [s + w for w in suffixes]


def main():
    prefix = "c"
    words = ["cat", "cards", "catalog", "dog", "cad", "froyo"]
    trie = Trie()
    for word in words:
        trie.insert(word)

    res = match_prefix(trie, prefix)
    pp(res)


if __name__ == '__main__':
    main()
