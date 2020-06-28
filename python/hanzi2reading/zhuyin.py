import re
from .syllable import Syllable

INITIALS = 'ㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏㄐㄑㄒㄓㄔㄕㄖㄗㄘㄙ'
MEDIALS = 'ㄧㄨㄩ'
FINALS = 'ㄚㄛㄜㄝㄞㄟㄠㄡㄢㄣㄤㄥ'
TONES = 'ˊˇˋ˙'
RE = re.compile("^(˙?)([" + INITIALS + "]?)([" + MEDIALS + "]?)([" + FINALS + "]?)([ˊˇˋ]?)(ㄦ?)$")

def parse(z):
    initial = 0
    medial = 0
    final = 0
    erhua = 0
    tone = 1
    match = re.match(RE,z)
    if match.group(1):
        tone = 5
    if match.group(2):
        initial = INITIALS.index(match.group(2)) + 1
    if match.group(3):
        medial = MEDIALS.index(match.group(3)) + 1
    if match.group(4):
        final = FINALS.index(match.group(4)) + 1
    if match.group(5):
        tone = TONES.index(match.group(5)) + 1
    if match.group(6):
        erhua = True
    return Syllable(initial,medial,final,tone,erhua)

def get(s):
    z = ''
    if s.tone == 5:
        z += '˙'
    if s.initial > 0:
        z += INITIALS[s.initial-1]
    if s.medial > 0:
        z += MEDIALS[s.medial-1]
    if s.final > 0:
        z += FINALS[s.final-1]
    if s.tone >= 2 and s.tone <= 4:
        z += TONES[s.tone-1]
    if s.erhua:
        z += '儿'
    return z