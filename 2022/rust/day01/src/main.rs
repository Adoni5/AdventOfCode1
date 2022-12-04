fn main() {
    let test_input = "1000
2000
3000

4000

5000
6000

7000
8000
9000

10000";
// Part 1 
    let input = std::fs::read_to_string("day01/day01.txt").unwrap();
    let x = input
        .split("\n\n")
        .map(|x| {
            x.split("\n")
                .into_iter()
                .filter_map(|s| s.parse::<u32>().ok())
                .sum::<u32>()
        })
        .max()
        .unwrap();
    println!("{:#?}", x);
// Part 2
let input = std::fs::read_to_string("day01/day01.txt").unwrap();
let mut x = input
    .split("\n\n")
    .map(|x| {
        x.split("\n")
            .into_iter()
            .filter_map(|s| s.parse::<u32>().ok())
            .sum::<u32>()
    })
    .collect::<Vec<u32>>();
x.sort();

let y = x.iter().rev()
    .take(3).sum::<u32>();
println!("{:#?}", y);
}
