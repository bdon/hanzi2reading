import unittest
from hanzi2reading.reading import Trie

class TestRead(unittest.TestCase):
    def test_basic(self):
        t = Trie()
        t.add('a',[1])
        self.assertEqual(t.get('a'),[1])

    def test_repeat(self):
        t = Trie()
        t.add('a',[1])
        self.assertEqual(t.get('aa'),[1,1])

    def test_different(self):
        t = Trie()
        t.add('a',[1])
        t.add('b',[2])
        self.assertEqual(t.get('ab'),[1,2])

    def test_entry(self):
        t = Trie()
        t.add('ba',[3,3])
        self.assertEqual(t.get('ba'),[3,3])

    def test_partial_match(self):
        t = Trie()
        t.add('a',[1])
        t.add('b',[2])
        t.add('e',[5])
        t.add('abc',[4,4,4])
        self.assertEqual(t.get('abe'),[1,2,5])

    def test_long(self):
        t = Trie()
        t.add('a',[1,2])
        self.assertEqual(t.get('aaa'),[1,2,1,2,1,2])

    def test_nomatch(self):
        t = Trie()
        t.add('a',[1,2])
        self.assertEqual(t.get('x'),[])
