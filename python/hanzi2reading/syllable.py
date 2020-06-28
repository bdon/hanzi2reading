from collections import namedtuple

SyllableData = namedtuple('SyllableData',['initial','medial','final','tone','er'])

class Syllable(SyllableData):
    def to_bytes(self):
        encoded = 0
        encoded |= (self.initial << 10)
        encoded |= (self.medial << 8)
        encoded |= (self.final << 4)
        encoded |= (self.tone << 1)
        encoded |= (self.er)
        return encoded.to_bytes(2,byteorder='little')

    @classmethod
    def from_bytes(cls,b):
        i = int.from_bytes(b,byteorder='little')
        initial = i >> 10 & 0b11111
        medial = i >> 8 & 0b11
        final = i >> 4 & 0b1111
        tone = i >> 1 & 0b111
        er = i & 0b1
        return cls(initial,medial,final,tone,er)