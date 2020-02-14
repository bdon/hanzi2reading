use std::borrow::Cow;
use std::env;
use serde::{Deserialize};
use serde_json::{Result, Value};
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
        for heteronym in &entry.heteronyms {
            if !heteronym["bopomofo"].is_null() {
                //println!("{} {}",entry.title,heteronym["bopomofo"].as_str().unwrap());
                readings.push(h2rdb::Reading{name:Cow::Borrowed(&entry.title),syllable:1234});
            }
        }
    }

    let dict = h2rdb::Dictionary{readings:readings};
    writer.write_message(&dict).expect("Cannot write Dictionary");
}
