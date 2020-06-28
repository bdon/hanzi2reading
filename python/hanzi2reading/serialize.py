import sys
from hanzi2reading import Syllable

def write(sink,entries):
    for entry in entries:
        # bit 1: high bit: is a proper noun (not used right now)
        # 3 bytes for headword bytes, 
        # 4 bytes for syllable bytes (erhua)
        headword_bytes = entry[0].encode('utf-8')
        num_headword_bytes = len(headword_bytes)
        num_syllables = len(entry[1])
        header = (num_headword_bytes << 4)
        header |= num_syllables
        sink.write(header.to_bytes(1,byteorder='little'))
        # the UTF-8 string (1 to 4 bytes each)
        sink.write(headword_bytes)
        for syllable in entry[1]:
            sink.write(syllable.to_bytes())

def read(source):
    header = int.from_bytes(source.read(1),byteorder='little')
    while header:
        num_headword_bytes = (header >> 4) & 0b111
        num_syllables = header & 0b1111
        headword = source.read(num_headword_bytes).decode('utf-8')
        syllables = []
        for i in range(0,num_syllables):
            syllables.append(Syllable.from_bytes(source.read(2)))
        yield headword, syllables
        header = int.from_bytes(source.read(1),byteorder='little')
