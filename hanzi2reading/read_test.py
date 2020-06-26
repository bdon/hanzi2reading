import unittest
from trie import Trie

class TestTrie(unittest.TestCase):

    def test_basic(self):
        t = Trie()
        t.add('a','a')
        self.assertEqual(t.get('a'),'a')

    def test_repeat(self):
        t = Trie()
        t.add('a','a')
        self.assertEqual(t.get('aa'),'aa')

    def test_different(self):
        t = Trie()
        t.add('a','a')
        t.add('b','b')
        self.assertEqual(t.get('ab'),'ab')

    def test_entry(self):
        t = Trie()
        t.add('ba','cc')
        self.assertEqual(t.get('ba'),'cc')

    def test_partial_match(self):
        t = Trie()
        t.add('a','a')
        t.add('b','b')
        t.add('e','e')
        t.add('abc','ddd')
        self.assertEqual(t.get('abe'),'abe')

    def test_long(self):
        t = Trie()
        t.add('a','ab')
        self.assertEqual(t.get('aaa'),'ababab')

if __name__ == '__main__':
    unittest.main()