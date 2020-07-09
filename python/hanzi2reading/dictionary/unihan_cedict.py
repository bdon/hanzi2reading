import sys
from hanzi2reading.dictionary import remove_redundant
from hanzi2reading.dictionary.unihan import parse as parse_unihan
from hanzi2reading.dictionary.cedict import parse as parse_cedict
from hanzi2reading.serialize import write

if __name__ == "__main__":
    unigrams = parse_unihan(sys.argv[1])
    print("Total unihan entries:", len(unigrams))

    entries = parse_cedict(sys.argv[2])
    entries = [e for e in entries if len(e[0]) > 1]
    print("Cedict bigrams+: ",len(entries))

    entries = unigrams + entries
    entries = remove_redundant(entries)
    print("Total:",len(entries))
    with open(sys.argv[3],'wb') as f:
        write(f,entries)