import sys
from trie import Trie

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
