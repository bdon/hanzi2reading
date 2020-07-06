import unittest
from io import BytesIO
from hanzi2reading import Syllable
import hanzi2reading.zhuyin as zhuyin
from hanzi2reading.serialize import read, write, to_bytes, from_bytes

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

    def test_to_bytes(self):
        b = to_bytes(zhuyin.parse('ㄎㄧㄤ'))
        self.assertEqual(len(b),2)
        self.assertEqual(b,b'\xb2\x29') # 0b 1011 0010 0010 1001 
        self.assertEqual(zhuyin.get(from_bytes(b)),'ㄎㄧㄤ')


