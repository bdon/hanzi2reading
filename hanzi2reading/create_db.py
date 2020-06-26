# Create a list of [unicode codepoint -> [reading sequence]] for each dictionary entry.
# assumes the heteronyms are listed in decreasing frequency.
# in this case, a character with multiple readings will have the first one chosen

# Compress the list of dictionary entries.
# any multi-character entry where all characters have a single reading is removed.

import json
import re
import sys

# remove all non-BMP characters
RE = re.compile(u'^[⺀-⺙⺛-⻳⼀-⿕々〇〡-〩〸-〺〻㐀-䶵一-鿃豈-鶴侮-頻並-龎]+$', re.UNICODE)

entries = []
chars = {}


with open('../moedict-data/dict-revised.json','r') as f:
  for entry in json.loads(f.read()):
    title = entry['title']
    if not RE.match(title):
        continue

    entries_with_bpmf = [x for x in entry['heteronyms'] if 'bopomofo' in x]
    if 'bopomofo' not in entry['heteronyms'][0]:
        print(entry['heteronyms'][0])
    if len(entries_with_bpmf) == 0:
        continue
    heteronym_1 = entries_with_bpmf[0]

    entries.append((title, heteronym_1['bopomofo']))
    if len(title) == 1:
        chars[title] = heteronym_1['bopomofo']


print(f"Dictionary entries: {len(entries)}")
print(f"Single reading chars: {len(chars)}")

redundant = 0
reduced = []
for entry in entries:
    if len(entry[0]) == 1:
        reduced.append(entry)
    else:
        parts = entry[1].split("\u3000")
        if [chars.get(c,'?') for c in entry[0]] == parts: # 櫈
            redundant = redundant + 1
        else:
            reduced.append(entry)

print(f"Eliminated entries: {redundant}")
print(f"Final entries: {len(reduced)}")
with open(sys.argv[1],'w') as f:
    for entry in reduced:
        f.write("{0},{1}\n".format(entry[0],entry[1].replace("\u3000",'')))


