from hanzi2reading import Syllable
import hanzi2reading.pinyin as pinyin

class Invalid(Exception):
    pass

def find_tone(s):
    if s.endswith('1'):
        return s[0:-1], 1
    if s.endswith('2'):
        return s[0:-1], 2
    if s.endswith('3'):
        return s[0:-1], 3
    if s.endswith('4'):
        return s[0:-1], 4
    if s.endswith('5'):
        return s[0:-1], 5
    raise Invalid('invalid pinyin_number',s)

def parse(p):
    if p[0].isupper():
        p = p.lower()

    base, tone = find_tone(p)
    initial, medial, final, er = pinyin.find_base(base)
    return Syllable(initial,medial,final,tone,er)
