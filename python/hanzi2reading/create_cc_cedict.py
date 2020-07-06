import sys
from pinyin_number import parse
from hanzi2reading.serialize import write
import re

entries = []

RE = re.compile(u'^(.+?) (.+?) \\[(.+?)\\]', re.UNICODE)

with open(sys.argv[1],'r') as f:
    for l in f.readlines():
        match = RE.match(l)
        if match:
            traditional = match.group(1)
            simplified = match.group(2)
            pinyin = match.group(3).replace('u:','ü')
            try:
                syllables = [parse(s) for s in pinyin.split(' ')]
                entries.append((traditional,syllables))
                if traditional != simplified:
                    entries.append((simplified,syllables))

            except Exception as e:
                pass
                # print(pinyin, e)

print("Entries:", len(entries))

with open(sys.argv[2],'wb') as f:
    write(f,entries)