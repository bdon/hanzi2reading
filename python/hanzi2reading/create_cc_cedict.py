import sys
from pinyin import parse
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
            pinyin = match.group(3)
            syllables = [parse(s) for s in pinyin.split(' ')]
            print(syllables)
