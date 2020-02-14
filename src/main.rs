use std::env;
use serde::{Deserialize};
use serde_json::{Result, Value};
use std::fs;

#[macro_use]
extern crate serde_derive;

#[derive(Deserialize)]
struct Entry {
    title:String,
    heteronyms:Vec<Value>
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let contents = fs::read_to_string(&args[1]).expect("should open file");
    let entries: Vec<Entry> = serde_json::from_str(&contents).expect("file should be proper JSON");

    for entry in &entries {
        if entry.title.chars().count() == 1 && entry.heteronyms.len() == 1 {
            println!("{} {}",entry.title, entry.heteronyms.len());
        }
    }
}
