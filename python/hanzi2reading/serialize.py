import sys
from hanzi2reading import Syllable

def to_bytes(s):
    encoded = 0
    encoded |= (s.initial << 10)
    encoded |= (s.medial << 8)
    encoded |= (s.final << 4)
    encoded |= (s.tone << 1)
    encoded |= (s.er)
    return encoded.to_bytes(2,byteorder='little')

def from_bytes(b):
    i = int.from_bytes(b,byteorder='little')
    initial = i >> 10 & 0b11111
    medial = i >> 8 & 0b11
    final = i >> 4 & 0b1111
    tone = i >> 1 & 0b111
    er = i & 0b1
    return Syllable(initial,medial,final,tone,er)

def write(sink,entries):
    for entry in entries:
        # bit 1: high bit: is a proper noun (not used right now)
        # 7 bytes for headword bytes, 
        # 8 bytes for syllable bytes (erhua)
        headword_bytes = entry[0].encode('utf-8')
        num_headword_bytes = len(headword_bytes)
        num_syllables = len(entry[1])
        sink.write(num_headword_bytes.to_bytes(1,byteorder='little'))
        sink.write(num_syllables.to_bytes(1,byteorder='little'))
        # the UTF-8 string (1 to 4 bytes each)
        sink.write(headword_bytes)
        for syllable in entry[1]:
            sink.write(to_bytes(syllable))

def read(source):
    num_headword_bytes = int.from_bytes(source.read(1),byteorder='little')
    while num_headword_bytes:
        num_syllables = int.from_bytes(source.read(1),byteorder='little')
        headword = source.read(num_headword_bytes).decode('utf-8')
        syllables = []
        for i in range(0,num_syllables):
            syllables.append(from_bytes(source.read(2)))
        yield headword, syllables
        num_headword_bytes = int.from_bytes(source.read(1),byteorder='little')
