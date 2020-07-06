from hanzi2reading.syllable import Syllable

INITIALS = ['b','p','m','f','d','t','n','l','g','k','h','j','q','x','zh','ch','sh','r','z','c','s']
# https://en.wikipedia.org/wiki/Zhuyin_table
MEDIALS_FINALS = [
    ['','a','o','e','ê','ai','ei','ao','ou','an','en','ang','eng'],
    ['i','ia','io','e','ie','iai','','iao','iu','ian','in','iang','ing'],
    ['u','ua','uo','','','uai','ui','','','uan','un','uang','ong'],
    ['ü','','','','üe','','','','','üan','ün','','iong']
]
NO_INITIAL = [
    [  '', 'a', 'o','e',  'ê', 'ai', 'ei', 'ao', 'ou',  'an', 'en', 'ang', 'eng'],
    ['yi','ya','yo', '', 'ye','yai',   '','yao','you', 'yan','yin','yang','ying'],
    ['wu','wa','wo', '',   '','wai','wei',   '',   '', 'wan','wen','wang','weng'],
    ['yu', '',   '', '','yue',   '',   '',   '',   '','yuan','yun',    '','yong']
]

TONE_CHARS = [
    ['āáǎà','a'],
    ['ēéěè','e'],
    ['īíǐì','i'],
    ['ōóǒò','o'],
    ['ūúǔù','u'],
    ['ǖǘǚǜ','ü']
]

# construct a lookup table from toneless pinyin to (INITIAL, MEDIAL, FINAL)

LOOKUP = {}
for medial, row in enumerate(NO_INITIAL):
    for final, p in enumerate(row):
        if p:
            LOOKUP[p] = (0,medial,final)

for medial, row in enumerate(MEDIALS_FINALS):
    for final, part2 in enumerate(row):
        if part2:
            for initial, part1 in enumerate(INITIALS):
                LOOKUP[part1 + part2] = (initial+1,medial,final)

EXCEPTIONS = {
    'ju':(12,3,0),
    'qu':(13,3,0),
    'xu':(14,3,0),
    'jue':(12,3,4),
    'que':(13,3,4),
    'xue':(14,3,4),
    'juan':(12,3,9),
    'quan':(13,3,9),
    'xuan':(14,3,9),
    'jun':(12,3,10),
    'qun':(13,3,10),
    'xun':(14,3,10),
    'zhi':(15,0,0),
    'chi':(16,0,0),
    'shi':(17,0,0),
    'ri':(18,0,0),
    'zi':(19,0,0),
    'ci':(20,0,0),
    'si':(21,0,0)
}

def parse(p):
    def find_tone(s):
        for vowel in TONE_CHARS:
            for idx, char in enumerate(vowel[0]):
                if char in s:
                    return s.replace(char,vowel[1]), idx+1
        return s, 5

    base, tone = find_tone(p)

    if base == 'er':
        return Syllable(0,0,0,tone,1)
    er = 0
    if base.endswith('r'):
        base = base[0:-1]
        er = 1

    if base in EXCEPTIONS:
        initial, medial, final = EXCEPTIONS[base]
    elif base in LOOKUP:
        initial, medial, final = LOOKUP[base]

    return Syllable(initial,medial,final,tone,er)


def get(s,tones=True):
    p = ''
    if s.initial == 0:
        p += NO_INITIAL[s.medial][s.final]
    else:
        p += INITIALS[s.initial-1]
        if s.initial in [12,13,14] and s.medial == 3 and s.final == 0:
            p += 'u'
        elif s.initial in [12,13,14] and s.medial == 3 and s.final == 4:
            p += 'ue'
        elif s.initial in [12,13,14] and s.medial == 3 and s.final == 9:
            p += 'uan'
        elif s.initial in [12,13,14] and s.medial == 3 and s.final == 10:
            p += 'un'
        elif s.initial in [15,16,17,18,19,20,21] and s.medial == 0 and s.final == 0:
            p += 'i'
        else:
            p += MEDIALS_FINALS[s.medial][s.final]

    if s.er:
        if s.initial == 0 and s.medial == 0 and s.final == 0:
            p += 'er'
        else:
            p += 'r'

    if tones:
        if s.tone <= 4:
            if 'a' in p:
                p = p.replace('a','āáǎà'[s.tone - 1])
            elif 'e' in p:
                p = p.replace('e','ēéěè'[s.tone - 1])
            elif 'o' in p:
                p = p.replace('o','ōóǒò'[s.tone - 1])
            elif 'iu' in p:
                p = p.replace('u','ūúǔù'[s.tone - 1])
            elif 'ui' in p:
                p = p.replace('i','īíǐì'[s.tone - 1])
            elif 'i' in p:
                p = p.replace('i','īíǐì'[s.tone - 1])
            elif 'u' in p:
                p = p.replace('u','ūúǔù'[s.tone - 1])
            elif 'ü' in p:
                p = p.replace('ü','ǖǘǚǜ'[s.tone - 1])

    return p