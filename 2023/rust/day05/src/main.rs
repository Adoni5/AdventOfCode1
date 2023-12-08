use std::collections::HashMap;

const INPUT: &str = include_str!("../test_input.txt");

fn main() {
    let mut split = INPUT.split("\n\n");

    let seeds = split
        .next()
        .unwrap()
        .split(": ")
        .nth(1)
        .unwrap()
        .split(' ')
        .map(|x| x.parse::<usize>())
        .collect::<Vec<_>>();
    // for block in blocks:
    // ranges = []
    // for line in block.splitlines()[1:]:
    //     ranges.append(list(map(int, line.split())))
    let HashMap::new();
}
