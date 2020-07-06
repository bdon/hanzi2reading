import sys

with open(sys.argv[1],'r') as f:
    for l in f.readlines():
        if l.startswith('#') or l == '\n':
            continue
        parts = l.strip().split('\t')
        if parts[1] == 'kMandarin':
            c = chr(int(parts[0][2:],16))
            pinyin = parts[2]
            print(c, pinyin)
