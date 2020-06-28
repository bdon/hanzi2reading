INITIALS = ['b','p','m','f','d','t','n','l','g','k','h','j','q','x','zh','ch','sh','r','z','c','s']
# https://en.wikipedia.org/wiki/Zhuyin_table
MEDIALS_FINALS = [
    ['','a','o','e','ê','ai','ei','ao','ou','an','en','ang','eng'],
    ['i','ia','io','e','ie','iai','','iao','iu','ian','in','iang','ing'],
    ['u','ua','uo','','','uai','ui','','','uan','un','uang','ong'],
    ['ü','','','','üe','','','','','üan','ün','','iong']
]
NO_INITIAL = [
    [  '', 'a', 'o','e',  'ê', 'ai', 'ei', 'ao',' ou',  'an', 'en', 'ang', 'eng'],
    ['yi','ya','yo', '', 'ye','yai',   '','yao','you', 'yan','yin','yang','ying'],
    ['wu','wa','wo', '',   '','wai','wei',   '',   '', 'wan','wen','wang','weng'],
    ['yu', '',   '', '','yue',   '',   '',   '',   '','yuan','yun',    '','yong']
]

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