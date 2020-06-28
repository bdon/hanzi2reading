import sys
from hanzi2reading.syllable import Syllable

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
            sink.write(syllable.to_bytes())

def read(source):
    num_headword_bytes = int.from_bytes(source.read(1),byteorder='little')
    while num_headword_bytes:
        num_syllables = int.from_bytes(source.read(1),byteorder='little')
        headword = source.read(num_headword_bytes).decode('utf-8')
        syllables = []
        for i in range(0,num_syllables):
            syllables.append(Syllable.from_bytes(source.read(2)))
        yield headword, syllables
        num_headword_bytes = int.from_bytes(source.read(1),byteorder='little')
