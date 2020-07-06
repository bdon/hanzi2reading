(function (root, factory) {
    if (typeof define === 'function' && define.amd) {
        define([], factory);
    } else if (typeof module === 'object' && module.exports) {
        module.exports = factory();
    } else {
        root.hanzi2reading = factory();
  }
}(typeof self !== 'undefined' ? self : this, function () {
    const PY_INITIALS = ['b','p','m','f','d','t','n','l','g','k','h','j','q','x','zh','ch','sh','r','z','c','s']
    const PY_MEDIALS_FINALS = [
        ['','a','o','e','ê','ai','ei','ao','ou','an','en','ang','eng'],
        ['i','ia','io','e','ie','iai','','iao','iu','ian','in','iang','ing'],
        ['u','ua','uo','','','uai','ui','','','uan','un','uang','ong'],
        ['ü','','','','üe','','','','','üan','ün','','iong']
    ]
    const PY_NO_INITIAL = [
        [  '', 'a', 'o','e',  'ê', 'ai', 'ei', 'ao',' ou',  'an', 'en', 'ang', 'eng'],
        ['yi','ya','yo', '', 'ye','yai',   '','yao','you', 'yan','yin','yang','ying'],
        ['wu','wa','wo', '',   '','wai','wei',   '',   '', 'wan','wen','wang','weng'],
        ['yu', '',   '', '','yue',   '',   '',   '',   '','yuan','yun',    '','yong']
    ]

    function pinyin(s) {
        var p = ''
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

        if (s[4]) {
            if (s[0] == 0 && s[1] == 0 && s[2] == 0) p += 'er'
            else p += 'r'
        }

        if (s[3] <= 4) {
            if (p.includes('a')) p = p.replace('a','āáǎà'[s[3] - 1])
            else if (p.includes('e')) p = p.replace('e','ēéěè'[s[3] - 1])
            else if (p.includes('o')) p = p.replace('o','ōóǒò'[s[3] - 1])
            else if (p.includes('iu')) p = p.replace('u','ūúǔù'[s[3] - 1])
            else if (p.includes('ui')) p = p.replace('i','īíǐì'[s[3] - 1])
            else if (p.includes('i')) p = p.replace('i','īíǐì'[s[3] - 1])
            else if (p.includes('u')) p = p.replace('u','ūúǔù'[s[3] - 1])
            else if (p.includes('ü')) p = p.replace('ü','ǖǘǚǜ'[s[3] - 1])
        }

        return p
    }

    const ZY_INITIALS = 'ㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏㄐㄑㄒㄓㄔㄕㄖㄗㄘㄙ'
    const ZY_MEDIALS = 'ㄧㄨㄩ'
    const ZY_FINALS = 'ㄚㄛㄜㄝㄞㄟㄠㄡㄢㄣㄤㄥ'
    const ZY_TONES = 'ˊˇˋ˙'

    function zhuyin(s) {
        var z = ''
        if (s[3] == 5) z += '˙'
        if (s[0] > 0) z += ZY_INITIALS[s[0]-1]
        if (s[1] > 0) z += ZY_MEDIALS[s[1]-1]
        if (s[2] > 0) z += ZY_FINALS[s[2]-1]
        if (s[0] == 0 && s[1] == 0 && s[2] == 0 && s[4]) z += 'ㄦ'
        if (s[3] >= 2 && s[3] <= 4) z += ZY_TONES[s[3]-2]
        if (!(s[0] == 0 && s[1] == 0 && s[2] == 0) && s[4]) z += 'ㄦ'
        return z
    }

    function add(root,headword,syllables) {
      var node = root
      for (var i = 0; i < headword.length; i++) {
          if (!(headword[i] in node[1])) {
              node[1][headword[i]] = [null,{}]
          }
          node = node[1][headword[i]]
          if (i == headword.length - 1) node[0] = syllables
      }
    }

    function annotate(trie,str) {
      var reading = [] 
      var i = 0
      while (i < str.length) {
          var j = i
          var node = trie
          var candidate = []
          var candidate_depth = 0
          var depth = 0
          if (!(str[j] in node[1])) {
              reading.push([str[i],null])
              i++
              continue
          }
          while (j < str.length && (str[j] in node[1])) {
              node = node[1][str[j]]
              depth = depth + 1
              if (node[0]) {
                  candidate_depth = depth
                  candidate = node[0]
              }
              j = j + 1
          }
          for (var u = 0; u < candidate_depth; u++) {
              reading.push([str[i+u],candidate[u]])
          }
          i = i + candidate_depth
      }
      return reading
    }

    class Reading {
      constructor(dict_path) {
        this.trie = fetch(dict_path).then(response => {
                return response.arrayBuffer()
            }).then(buffer => {
                const decoder = new TextDecoder("utf-8")
                const view = new Uint8Array(buffer)
                var i = 0
                var root = [null,{}]
                while (i < view.length) {
                    var num_headword_bytes = view[i++]
                    var num_syllables = view[i++]
                    var headword = decoder.decode(view.subarray(i,i+num_headword_bytes))
                    i+= num_headword_bytes
                    var syllables = []
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
                    add(root,headword,syllables)
                }
                return root
            })
      }

      annotate(s) {
        return new Promise((resolve,reject) => {
           this.trie.then(t => {
             resolve(annotate(t,s))
           })
        })
      }
    }

    return {Reading:Reading,zhuyin:zhuyin,pinyin:pinyin};
}));