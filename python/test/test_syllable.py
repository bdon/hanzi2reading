import unittest
from hanzi2reading import Syllable
import hanzi2reading.zhuyin as zhuyin

class TestSyllable(unittest.TestCase):
    def test_first_tone(self):
        s = zhuyin.parse('ㄎㄧㄤ')
        self.assertEqual(s.initial,10)
        self.assertEqual(s.medial,1)
        self.assertEqual(s.final,11)
        self.assertEqual(s.tone,1)
        self.assertFalse(s.er)
        self.assertEqual(zhuyin.get(s),'ㄎㄧㄤ')

    def test_er(self):
        self.assertEqual(zhuyin.get(zhuyin.parse("ㄔㄨㄦ")),"ㄔㄨㄦ")
        self.assertEqual(zhuyin.get(zhuyin.parse("˙ㄊㄡㄦ")),"˙ㄊㄡㄦ")
        self.assertEqual(zhuyin.get(zhuyin.parse("ㄔㄚˊㄦ")),"ㄔㄚˊㄦ")
        self.assertEqual(zhuyin.get(zhuyin.parse("ㄦˇ")),"ㄦˇ")

    def test_fifth_tone(self):
        s = zhuyin.parse('˙ㄇㄚ')
        self.assertEqual(s.initial,3)
        self.assertEqual(s.medial,0)
        self.assertEqual(s.final,1)
        self.assertEqual(s.tone,5)
        self.assertFalse(s.er)
        self.assertEqual(zhuyin.get(s),'˙ㄇㄚ')