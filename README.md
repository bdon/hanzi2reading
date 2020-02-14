# hanzi2reading

## Design goals
* Annotation of Chinese characters with Standard Mandarin (國語/普通話）readings, script-agnostic
* Should work offline, and database format should be as compact as possible - e.g. Protocol Buffers loaded by WebAssembly
* Should support word-based disambiguation of characters with multiple readings
* separation of code and data - dictionary backend should be swappable

## Limitations
* Word segmentation is a non-goal.
* Target should be good performance for non-sentence inputs, without needing part-of-speech classification, e.g. 得

## Notes
* https://www.unicode.org/reports/tr38/#N1019C
* https://languagelog.ldc.upenn.edu/nll/?p=45843

## Resources
* https://github.com/mozillazg/python-pinyin (SC only, data embedded in code)
* https://github.com/tsroten/dragonmapper (data is in large CSV files, Python only)
* https://github.com/g0v/moedict-data
* https://cc-cedict.org/editor/editor.php

