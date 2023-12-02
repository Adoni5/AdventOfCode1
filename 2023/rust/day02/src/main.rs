const INPUT: &str = include_str!("../input.txt");
use regex::Regex;
use std::collections::HashMap;
fn main() {
    let re = Regex::new(r"(?<count>\d+) (?<colour>blue|red|green)").unwrap();
    let hashy = HashMap::from([("red", 12), ("blue", 14), ("green", 13)]);
    let p1: usize = INPUT
        .lines()
        .enumerate()
        .map(|(index, line)| {
            let mut too_big = false;
            re.captures_iter(line).for_each(|caps| {
                let (_, [count, colour]) = caps.extract();
                if let Some(x) = hashy.get(colour) {
                    if count.parse::<i32>().unwrap() > *x {
                        too_big = true;
                        println!("{} is too big", colour);
                    }
                }
            });
            if !too_big {
                index + 1
            } else {
                0
            }
        })
        .sum();

    println!("Hello, world!, p1: {}", p1);

    // P2
    let p2: usize = INPUT
        .lines()
        .map(|line| {
            let mut too_big = false;
            let mut hashy = HashMap::from([("red", 0), ("blue", 0), ("green", 0)]);

            re.captures_iter(line).for_each(|caps| {
                let (_, [count, colour]) = caps.extract();
                if let Some(x) = hashy.get_mut(colour) {
                    if count.parse::<usize>().unwrap() > *x {
                        too_big = true;
                        *x = count.parse::<usize>().unwrap();
                    }
                }
            });
            hashy.values().product::<usize>()
        })
        .sum();
    println!("p2 sum {:?}", p2);
}
