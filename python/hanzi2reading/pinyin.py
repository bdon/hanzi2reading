INITIALS = ['b','p','m','f','d','t','n','l','g','k','h','j','q','x','zh','ch','sh','r','z','c','s']
MEDIALS = ['i','u','ü']
FINALS = ['a','o','e','ie','ai','ei','ao','ou','an','en','ang','eng']
NO_INITIAL = [
    [  '', 'a', 'o','e',  'ê', 'ai', 'ei', 'ao',' ou',  'an', 'en', 'ang', 'eng'],
    ['yi','ya',  '', '', 'ye',   '',   '','yao','you', 'yan','yin','yang','ying'],
    ['wu','wa','wo', '',   '','wai','wei',   '',   '', 'wan','wen','wang','weng'],
    ['yu', '',   '', '','yue',   '',   '',   '',   '','yuan','yun',    '','yong']
]

# https://en.wikipedia.org/wiki/Pinyin_table
def get(s):
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
        elif s.medial == 1 and s.final == 4:
            p += 'ie'
        elif s.medial == 1 and s.final == 8:
            p += 'iu'
        elif s.medial == 2 and s.final == 6:
            p += 'ui'
        elif s.medial == 2 and s.final == 10:
            p += 'un'
        else:
            if s.medial > 0:
                p += MEDIALS[s.medial-1]
            if s.final > 0:
                p += FINALS[s.final-1]

    if 'a' in p:
        p = p.replace('a','āáǎà'[s.tone - 1])
    elif 'e' in p:
        p = p.replace('e','ēéěè'[s.tone - 1])
    elif 'o' in p:
        p = p.replace('o','ōóǒò'[s.tone - 1])
    elif 'iu' in p:
        p = p.replace('iu','iū')
    elif 'ui' in p:
        p = p.replace('ui','uī')
    elif 'i' in p:
        p = p.replace('i','īíǐì'[s.tone - 1])
    elif 'u' in p:
        p = p.replace('u','ūúǔù'[s.tone - 1])
    elif 'ü' in p:
        p = p.replace('ü','ǖǘǚǜ'[s.tone - 1])

    return p