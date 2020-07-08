import sys
from hanzi2reading.pinyin import get
from hanzi2reading.pinyin_number import parse as parse_pinyin_number
from hanzi2reading.serialize import write
from hanzi2reading.dictionary import BMP_HANZI, fill_unigrams, remove_redundant
import re

RE = re.compile(u'^(.+?) (.+?) \\[(.+?)\\]', re.UNICODE)

# returns a list of (headword, [syllable]) entries
def parse(fname):
    entries = []
    seen = set()
    with open(fname) as f:
        for l in f.readlines():
            match = RE.match(l)
            if match:
                traditional = match.group(1)
                simplified = match.group(2)
                if len(traditional) > 8:
                    continue
                if not BMP_HANZI.match(traditional):
                    continue
                pinyin = match.group(3).replace('u:','ü')
                try:
                    syllables = [parse_pinyin_number(s) for s in pinyin.split(' ')]
                    if traditional not in seen:
                        entries.append((traditional,syllables))
                        seen.add(traditional)
                    if simplified not in seen:
                        entries.append((simplified,syllables))
                        seen.add(simplified)
                except Exception as e:
                    pass
    return entries

if __name__ == "__main__":
    entries = parse(sys.argv[1])
    print("Entries: ",len(entries))
    entries = fill_unigrams(entries)
    entries = remove_redundant(entries)
    print("Total:",len(entries))
    with open(sys.argv[2],'wb') as f:
        write(f,entries)
