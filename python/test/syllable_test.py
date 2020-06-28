import unittest
from hanzi2reading import Syllable
import hanzi2reading.zhuyin as zhuyin
import hanzi2reading.pinyin as pinyin

class TestSyllable(unittest.TestCase):
    def test_first_tone(self):
        s = zhuyin.parse('ㄎㄧㄤ')
        self.assertEqual(s.initial,10)
        self.assertEqual(s.medial,1)
        self.assertEqual(s.final,11)
        self.assertEqual(s.tone,1)
        self.assertFalse(s.erhua)
        self.assertEqual(zhuyin.get(s),'ㄎㄧㄤ')

    def test_fifth_tone(self):
        s = zhuyin.parse('˙ㄇㄚ')
        self.assertEqual(s.initial,3)
        self.assertEqual(s.medial,0)
        self.assertEqual(s.final,1)
        self.assertEqual(s.tone,5)
        self.assertFalse(s.erhua)
        self.assertEqual(zhuyin.get(s),'˙ㄇㄚ')

    def test_to_bytes(self):
        b = zhuyin.parse('ㄎㄧㄤ').to_bytes()
        self.assertEqual(len(b),2)
        self.assertEqual(b,b'\x29\xb2') # 0b 0010 1001 1011 0010
        self.assertEqual(zhuyin.get(Syllable.from_bytes(b)),'ㄎㄧㄤ')

    def test_pinyin(self):
        def zp(z,p):
            self.assertEqual(pinyin.get(zhuyin.parse(z)),p)

        zp('ㄧ','yī')
        zp('ㄧㄡ','yōu')
        zp('ㄧㄣ','yīn')
        zp('ㄧㄥ','yīng')
        zp('ㄨ','wū')
        zp('ㄨㄟ','wēi')
        zp('ㄨㄣ','wēn')

        zp('ㄋㄩ','nǖ')
        zp('ㄐㄩ','jū')
        zp('ㄐㄩㄝ','juē')
        zp('ㄐㄩㄢ','juān')
        zp('ㄐㄩㄣ','jūn')

        zp('ㄐㄧㄝ','jiē')
        zp('ㄌㄧㄡ','liū')
        zp('ㄉㄨㄟ','duī')
        zp('ㄉㄨㄣ','dūn')

        zp('ㄎㄧㄤ','kiāng')
        zp('ㄉㄨㄤ','duāng')

if __name__ == '__main__':
    unittest.main()