import sys
from pinyin import get
from pinyin_number import parse
from hanzi2reading.serialize import write
import re

entries = []

HANZI = re.compile(u'^[⺀-⺙⺛-⻳⼀-⿕々〇〡-〩〸-〺〻㐀-䶵一-鿃豈-鶴侮-頻並-龎]+$', re.UNICODE)
RE = re.compile(u'^(.+?) (.+?) \\[(.+?)\\]', re.UNICODE)

unigrams = {}

with open(sys.argv[1],'r') as f:
    for l in f.readlines():
        match = RE.match(l)
        if match:
            traditional = match.group(1)
            simplified = match.group(2)
            if len(traditional) > 8:
                continue
            if not HANZI.match(traditional):
                continue
            pinyin = match.group(3).replace('u:','ü')
            try:
                syllables = [parse(s) for s in pinyin.split(' ')]
                if len(traditional) == 1:
                    if traditional[0] in unigrams:
                        continue
                    unigrams[traditional[0]] = syllables[0]
                entries.append((traditional,syllables))
                if traditional != simplified:
                    entries.append((simplified,syllables))

            except Exception as e:
                pass


# infill any 1-grams that only appear in a 2-gram or mode
# TODO does this need a new entry?
for entry in entries:
    if len(entry[0]) > 1:
        for idx, char in enumerate(entry[0]):
            if char not in unigrams:
                unigrams[char] = entry[1][idx]

print("Entries:", len(entries))
print("Num unigrams:", len(unigrams))

redundant = 0
reduced = []
for entry in entries:
    if len(entry[0]) == 1:
        reduced.append(entry)
    else:
        if [unigrams[c] for c in entry[0]] == entry[1]:
            redundant = redundant + 1
        else:
            reduced.append(entry)

print("Redundant:", redundant)
print("Total:",len(reduced))
with open(sys.argv[2],'wb') as f:
    write(f,reduced)