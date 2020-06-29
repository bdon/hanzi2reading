PY_INITIALS = ['b','p','m','f','d','t','n','l','g','k','h','j','q','x','zh','ch','sh','r','z','c','s']
PY_MEDIALS_FINALS = [
    ['','a','o','e','ê','ai','ei','ao','ou','an','en','ang','eng'],
    ['i','ia','io','e','ie','iai','','iao','iu','ian','in','iang','ing'],
    ['u','ua','uo','','','uai','ui','','','uan','un','uang','ong'],
    ['ü','','','','üe','','','','','üan','ün','','iong']
]
PY_NO_INITIAL = [
    [  '', 'a', 'o','e',  'ê', 'ai', 'ei', 'ao',' ou',  'an', 'en', 'ang', 'eng'],
    ['yi','ya','yo', '', 'ye','yai',   '','yao','you', 'yan','yin','yang','ying'],
    ['wu','wa','wo', '',   '','wai','wei',   '',   '', 'wan','wen','wang','weng'],
    ['yu', '',   '', '','yue',   '',   '',   '',   '','yuan','yun',    '','yong']
]

function pinyin(s) {
    p = ''
    if (s[0] == 0) p += PY_NO_INITIAL[s[1]][s[2]]
    else {
        p += PY_INITIALS[s[0]-1]
        if (s[0] >= 12 && s[0] <= 14 && s[1] == 3 && s[2] == 0) p += 'u'
        else if (s[0] >= 12 && s[0] <= 14 && s[1] == 3 && s[2] == 4) p += 'ue'
        else if (s[0] >= 12 && s[0] <= 14 && s[1] == 3 && s[2] == 9) p += 'uan'
        else if (s[0] >= 12 && s[0] <= 14 && s[1] == 3 && s[2] == 10) p += 'un'
        else if (s[0] >= 15 && s[0] <= 21 && s[1] == 0 && s[2] == 0) p += 'i'
        else p += PY_MEDIALS_FINALS[s[1]][s[2]]
    }

    if (s[3] <= 4) {
        if (p.includes('a')) p = p.replace('a','āáǎà'[s[3] - 1])
        else if (p.includes('e')) p = p.replace('e','ēéěè'[s[3] - 1])
        else if (p.includes('u')) p = p.replace('u','ūúǔù'[s[3] - 1])
        else if (p.includes('iu')) p = p.replace('u','ūúǔù'[s[3] - 1])
        else if (p.includes('ui')) p = p.replace('i','īíǐì'[s[3] - 1])
        else if (p.includes('u')) p = p.replace('u','ūúǔù'[s[3] - 1])
        else if (p.includes('ü')) p = p.replace('ü','ǖǘǚǜ'[s[3] - 1])
    }
    return p
}

fetch('./moedict.h2r').then(response => {
    response.arrayBuffer().then(buffer => {
        const decoder = new TextDecoder("utf-8")
        const view = new Uint8Array(buffer)
        var i = 0
        while (i < view.length) {
            num_headword_bytes = view[i++]
            num_syllables = view[i++]
            var headword = decoder.decode(view.subarray(i,i+num_headword_bytes))
            i+= num_headword_bytes
            syllables = []
            for (var j = 0; j < num_syllables; j++) {
                var b1 = view[i]
                var b2 = view[i+1]
                syllables.push([
                    b2 >> 2 & 0b11111,
                    b2 & 0b11,
                    b1 >> 4 & 0b1111,
                    b1 >> 1 & 0b111,
                    b1 & 0b1
                ])
                i+= 2
            }
            if (i > 10000) return
        }
    })
})
