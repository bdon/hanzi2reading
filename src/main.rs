use std::borrow::Cow;
use std::env;
use serde_json::{Value};
use std::fs;
use std::fs::File;
use quick_protobuf::Writer;

#[macro_use]
extern crate serde_derive;

#[derive(Deserialize)]
struct Entry {
    title:String,
    heteronyms:Vec<Value>
}
 
mod h2rdb;

fn main() {
    let args: Vec<String> = env::args().collect();
    let contents = fs::read_to_string(&args[1]).expect("should open file");
    let entries: Vec<Entry> = serde_json::from_str(&contents).expect("file should be proper JSON");

    let mut r = File::create("h2r.db").expect("Cannot create file");
    let mut writer = Writer::new(&mut r);

    let mut readings = Vec::new();

    for entry in &entries {
        if entry.title.chars().count() < 3 {
            for heteronym in &entry.heteronyms {
                if !heteronym["bopomofo"].is_null() {
                    println!("{} {}",entry.title,heteronym["bopomofo"].as_str().unwrap());
                    readings.push(h2rdb::Reading{name:Cow::Borrowed(&entry.title),syllable:1234});
                }
            }
        }
    }

    let dict = h2rdb::Dictionary{readings:readings};
    writer.write_message(&dict).expect("Cannot write Dictionary");
}

// initials medials finals  tones erhua
// 0                        ˙ 5
// 1  ㄅ b  ㄧ i     ㄚ a      1   ㄦ er
// 2  ㄆ p  ㄨ u     ㄛ o    ˊ 2
// 3  ㄇ m  ㄩ ü     ㄜ e    ˇ 3
// 4  ㄈ f           ㄝ ê    ˋ 4
// 5  ㄉ d           ㄞ ai
// 6  ㄊ t           ㄟ ei
// 7  ㄋ n           ㄠ ao
// 8  ㄌ l           ㄡ ou
// 9  ㄍ g           ㄢ an
// 10 ㄎ k           ㄣ en
// 11 ㄏ h           ㄤ ang
// 12 ㄐ j           ㄥ eng
// 13 ㄑ q
// 14 ㄒ x
// 15 ㄓ zh
// 16 ㄔ ch
// 17 ㄕ sh
// 18 ㄖ r
// 19 ㄗ z
// 20 ㄘ c
// 21 ㄙ s
//
// example encodings:
// 兒 : ˊㄦ/er2 becomes [0,0,0,2,1]
// 串 : ㄔㄨㄢˋㄦ/chuanr4 becomes [16,2,9,4,1]

pub fn convert(s:&str) -> u32 {
    return 0;
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_add() {
        assert_eq!(convert("儿"),0x1);
    }
}