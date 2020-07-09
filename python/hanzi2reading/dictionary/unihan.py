import sys
from hanzi2reading.pinyin import parse as parse_pinyin
from hanzi2reading.serialize import write

def parse(fname):
    entries = []
    with open(fname,'r') as f:
        for l in f.readlines():
            if l.startswith('#') or l == '\n':
                continue
            parts = l.strip().split('\t')
            if parts[1] == 'kMandarin':
                c = chr(int(parts[0][2:],16))
                pinyin = parts[2]
                if ' ' in pinyin:
                   pinyin = pinyin.split(' ')[0] # prefer zh-hans (1 is zh-hant)
                try:
                    entries.append((c,[parse_pinyin(pinyin)]))
                except Exception:
                    print("Ignored invalid pinyin:", c,pinyin)
    return entries

if __name__ == "__main__":
    entries = parse(sys.argv[1])
    print("Total entries:", len(entries))
    with open(sys.argv[2],'wb') as f:
        write(f,entries)
