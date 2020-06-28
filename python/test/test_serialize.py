import unittest
from io import BytesIO
from hanzi2reading.syllable import Syllable
from hanzi2reading.serialize import read, write

class TestFile(unittest.TestCase):
    def test_serialize(self):
        entries = [('夯',[Syllable(11,0,11,1,0)])]
        b = BytesIO()
        write(b,entries)
        b.seek(0)
        self.assertEqual(len(b.read()),2+3+2)
        b.seek(0)
        for headword, syllables in read(b):
            self.assertEqual(headword,'夯')
            self.assertEqual(syllables[0].initial,11)
            self.assertEqual(syllables[0].final,11)
