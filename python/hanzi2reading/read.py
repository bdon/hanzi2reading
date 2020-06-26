import sys

class TrieNode:
    def __init__(self):
        self.val = None
        self.children = {}

class Trie:
    def __init__(self):
        self._t = TrieNode()

    def add(self,s,value):
        node = self._t
        for idx,c in enumerate(s):
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            if idx == len(s)-1:
                node.val = value

    def get(self,s):
        reading = ''
        i = 0
        while i < len(s):
            j = i
            node = self._t
            candidate = ''
            candidate_depth = 0
            depth = 0
            while j < len(s) and s[j] in node.children:
                node = node.children[s[j]]
                depth = depth + 1
                if node.val:
                    candidate_depth = depth
                    candidate = node.val
                j = j + 1

            reading = reading + candidate
            i = i + candidate_depth

        return reading

class Reading:
    def __init__(self,fname):
        self._trie = Trie()

        with open(fname,'r') as f:
            for x in f.readlines():
                pair = x.rstrip().split(',')
                self._trie.add(pair[0],pair[1])

    def get(self,hanzi):
        return self._trie.get(hanzi)

r = Reading(sys.argv[1])
print(r.get('行'))
print(r.get('臺'))
print(r.get('台灣銀行'))
