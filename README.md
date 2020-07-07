# hanzi2reading

A library for transcribing strings of Chinese characters to their readings in Mandarin.

An example JavaScript application: http://bdon.org/hanzireader/

* Disambiguates multiple-reading characters based on a dictionary.
* Defines a binary format for dictionaries that can be loaded at runtime.
  * The dictionary format is designed to be as compact as possible.
  * Dictonaries are agnostic to Traditional/Simplified script and transliteration format, and store pronunciations as 2-byte syllable sequences based on Zhuyin.
  * A typical dictionary CC-CEDICT in this format is around 300 kB, or less than 200 kB Brotli-compressed, meaning it is practical to load the entire dictionary once over the web and then perform transcription without any network communication.
* The library and dictionary can be shared across multiple programming languages. Python and JavaScript are supported right now.

## Installation

Javascript: `npm install hanzi2reading`
Python: `pip install hanzi2reading`

## Dictionaries

* CC-CEDICT. Licensed CC-BY-SA.
* Moedict. Licensed CC-BY-ND. https://github.com/g0v/moedict-data/blob/master/README.md
* Unihan database, which only contains 1-grams only. Licensed under Unicode License.

## Limitations

* This library only does dictionary-based lookups of character sequences. It does not attempt to disambiguate readings based on parts of speech, which is necessary for transcribing complete sentences. 
* Word segmentation and proper nouns for formatted Pinyin is not supported, but may be in the future.

## Binary Syllable format

Part | Bits
--- | ---
Initial | 5
Medial | 2
Final | 4
Tone | 3
Er | 1

## Notes
* https://www.unicode.org/reports/tr38/#N1019C
* https://languagelog.ldc.upenn.edu/nll/?p=45843

## Resources
* https://github.com/mozillazg/python-pinyin (SC only, data embedded in code)
* https://github.com/tsroten/dragonmapper (data is in large CSV files, Python only)
* https://github.com/g0v/moedict-data
* https://cc-cedict.org/editor/editor.php
* https://chrome.google.com/webstore/detail/zhongwen-chinese-english/kkmlkkjojmombglmlpbpapmhcaljjkde
* https://github.com/skishore/makemeahanzi

