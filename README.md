# hanzi2reading

## Design goals
* Annotation of Chinese characters with Standard Mandarin (國語/普通話）readings, script-agnostic
* Should work offline, and database format should be as compact as possible - e.g. Protocol Buffers loaded by WebAssembly
* Should support word-based disambiguation of characters with multiple readings
* separation of code and data - dictionary backend should be swappable
* Word segmentation is a non-goal

## Notes
* https://www.unicode.org/reports/tr38/#N1019C
* https://languagelog.ldc.upenn.edu/nll/?p=45843

## Resources
* https://github.com/mozillazg/python-pinyin (SC only, data embedded in code)
* https://github.com/g0v/moedict-data
* https://cc-cedict.org/editor/editor.php
