

import re

BMP_HANZI = re.compile(u'^[⺀-⺙⺛-⻳⼀-⿕々〇〡-〩〸-〺〻㐀-䶵一-鿃豈-鶴侮-頻並-龎]+$', re.UNICODE)

# infill any 1-grams that only appear in a 2-gram or mode
def fill_unigrams(entries):
    unigrams = {}
    for entry in entries:
        if len(entry[0]) == 1:
            unigrams[entry[0]] = entry[1][0]

    infill = {}
    for entry in entries:
        if len(entry[0]) > 1:
            for idx, char in enumerate(entry[0]):
                if char not in unigrams:
                    infill[char] = [entry[1][idx]]

    print("Infill unigrams: ",len(infill))
    for headword, syllables in infill.items():
        entries.append((headword,syllables))

    return entries

def remove_redundant(entries):
    unigrams = {}
    for entry in entries:
        if len(entry[0]) == 1:
            unigrams[entry[0]] = entry[1][0]

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

    print("Redundant: ",len(entries) - len(reduced))
    return reduced

