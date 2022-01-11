import unittest
from hanzi2reading import Syllable
import hanzi2reading.zhuyin as zhuyin
import hanzi2reading.hanyu_pinyin as hanyu_pinyin
import hanzi2reading.hanyu_pinyin_number as hanyu_pinyin_number

class TestPinyin(unittest.TestCase):
    def test_pinyin(self):
        def zp(z,p):
            self.assertEqual(hanyu_pinyin.get(zhuyin.parse(z)),p)
            self.assertEqual(zhuyin.get(hanyu_pinyin.parse(p)),z)
        zp('ㄧ','yī')
        zp('ㄧㄡ','yōu')
        zp('ㄧㄣ','yīn')
        zp('ㄧㄥ','yīng')
        zp('ㄨ','wū')
        zp('ㄨㄟ','wēi')
        zp('ㄨㄣ','wēn')
        zp('ㄋㄩ','nǖ')
        zp('ㄐㄩ','jū')
        zp('ㄐㄩㄝ','juē')
        zp('ㄐㄩㄢ','juān')
        zp('ㄐㄩㄣ','jūn')

        zp('ㄐㄧㄝ','jiē')
        zp('ㄌㄧㄡ','liū')

        zp('ㄉㄨㄟ','duī')
        zp('ㄉㄨㄟˊ','duí')
        zp('ㄉㄨㄟˇ','duǐ')
        zp('ㄉㄨㄟˋ','duì')
        zp('˙ㄉㄨㄟ','dui')

        zp('ㄉㄨㄣ','dūn')
        zp('ㄒㄧㄥˊ','xíng')
        zp('ㄒㄩㄥˊ','xióng')
        zp('ㄠ','āo')
        zp('ㄙˇ','sǐ')
        zp('ㄦ','ēr')
        zp('ㄧㄞˊ','yái')
        zp('ㄈㄢˋㄦ','fànr')
        zp('ㄩㄥ','yōng')
        zp('ㄏㄜˊ','hé')

    def test_nonstandard_pinyin(self):
        def zp(z,p):
            self.assertEqual(hanyu_pinyin.get(zhuyin.parse(z)),p)
        zp('ㄎㄧㄤ','kiāng')
        zp('ㄉㄨㄤ','duāng')
        zp('ㄧㄛ','yō')

    def test_propernoun_pinyin(self):
        # whether or not the syllable is capitalized is not stored yet.
        self.assertEqual(zhuyin.get(hanyu_pinyin.parse('Yī')),'ㄧ')

    def test_pinyin_number(self):
        self.assertEqual(zhuyin.get(hanyu_pinyin_number.parse('yi1')),'ㄧ')
        self.assertEqual(zhuyin.get(hanyu_pinyin_number.parse('Yi1')),'ㄧ')