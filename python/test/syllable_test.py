import unittest
import re
from collections import namedtuple

SyllableData = namedtuple('SyllableData',['initial','medial','final','tone','erhua'])

class Syllable(SyllableData):
    def to_bytes(self):
        encoded = 0
        encoded |= (self.initial << 10)
        encoded |= (self.medial << 8)
        encoded |= (self.final << 4)
        encoded |= (self.tone << 1)
        encoded |= (self.erhua)
        return encoded.to_bytes(2,byteorder='big')

    @classmethod
    def from_bytes(cls,b):
        i = int.from_bytes(b,byteorder='big')
        initial = i >> 10 & 0b11111
        medial = i >> 8 & 0b11
        final = i >> 4 & 0b1111
        tone = i >> 1 & 0b111
        erhua = i & 0b1
        return cls(initial,medial,final,tone,erhua)

Z_INITIALS = 'ㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏㄐㄑㄒㄓㄔㄕㄖㄗㄘㄙ'
Z_MEDIALS = 'ㄧㄨㄩ'
Z_FINALS = 'ㄚㄛㄜㄝㄞㄟㄠㄡㄢㄣㄤㄥ'
Z_TONES = 'ˊˇˋ˙'
Z_RE = re.compile("^(˙?)([" + Z_INITIALS + "]?)([" + Z_MEDIALS + "]?)([" + Z_FINALS + "]?)([ˊˇˋ]?)(ㄦ?)$")

def from_zhuyin(z):
    initial = 0
    medial = 0
    final = 0
    erhua = 0
    tone = 1
    match = re.match(Z_RE,z)
    if match.group(1):
        tone = 5
    if match.group(2):
        initial = Z_INITIALS.index(match.group(2)) + 1
    if match.group(3):
        medial = Z_MEDIALS.index(match.group(3)) + 1
    if match.group(4):
        final = Z_FINALS.index(match.group(4)) + 1
    if match.group(5):
        tone = Z_TONES.index(match.group(5)) + 1
    if match.group(6):
        erhua = True
    return Syllable(initial,medial,final,tone,erhua)

def to_zhuyin(s):
    z = ''
    if s.tone == 5:
        z += '˙'
    if s.initial > 0:
        z += Z_INITIALS[s.initial-1]
    if s.medial > 0:
        z += Z_MEDIALS[s.medial-1]
    if s.final > 0:
        z += Z_FINALS[s.final-1]
    if s.tone >= 2 and s.tone <= 4:
        z += Z_TONES[s.tone-1]
    if s.erhua:
        z += '儿'
    return z

class TestSyllable(unittest.TestCase):
    def test_first_tone(self):
        s = from_zhuyin('ㄎㄧㄤ')
        self.assertEqual(s.initial,10)
        self.assertEqual(s.medial,1)
        self.assertEqual(s.final,11)
        self.assertEqual(s.tone,1)
        self.assertFalse(s.erhua)
        self.assertEqual(to_zhuyin(s),'ㄎㄧㄤ')

    def test_fifth_tone(self):
        s = from_zhuyin('˙ㄇㄚ')
        self.assertEqual(s.initial,3)
        self.assertEqual(s.medial,0)
        self.assertEqual(s.final,1)
        self.assertEqual(s.tone,5)
        self.assertFalse(s.erhua)
        self.assertEqual(to_zhuyin(s),'˙ㄇㄚ')

    def test_to_bytes(self):
        b = from_zhuyin('ㄎㄧㄤ').to_bytes()
        self.assertEqual(len(b),2)
        self.assertEqual(b,b'\x29\xb2') # 0b 0010 1001 1011 0010
        self.assertEqual(to_zhuyin(Syllable.from_bytes(b)),'ㄎㄧㄤ')

if __name__ == '__main__':
    unittest.main()