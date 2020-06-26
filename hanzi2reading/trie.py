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