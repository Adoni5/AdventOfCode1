use regex::Regex;

const INPUT: &str = include_str!("../input.txt");
fn main() {
    println!("Hello, world! It's advent of code aaaah");
    let sum: usize = INPUT
        .lines()
        .map(|line| {
            let num_string = line.chars().filter(|x| x.is_numeric()).collect::<Vec<_>>();
            format!("{}{}", num_string[0], num_string[num_string.len() - 1])
                .parse::<usize>()
                .unwrap()
        })
        .sum::<usize>();
    println!("p1  sum: {}", sum);

    // P2

    let re = Regex::new(r"(one|two|three|four|five|six|seven|eight|nine|[1-9])").unwrap();
    let p2: usize = INPUT
        .lines()
        .map(|hay| {
            let mut nums = vec![];
            // slice indx the string to do overlapping regexes
            let mut offset: usize = 0;
            // DO the regex on each slice until turn until we don't match
            while let Some(mat) = re.find(&hay[offset..]) {
                // println!("{} {} {}", mat.start(), mat.end(), mat.as_str());
                let d = mat.as_str().len() - 1;
                offset += mat.end() - d;

                // println!("{} {}", &hay[offset..hay.len()], mat.as_str());
                // println!("offset {}", offset);
                let num = match mat.as_str() {
                    "one" => 1,
                    "two" => 2,
                    "three" => 3,
                    "four" => 4,
                    "five" => 5,
                    "six" => 6,
                    "seven" => 7,
                    "eight" => 8,
                    "nine" => 9,
                    _ => mat.as_str().parse::<usize>().unwrap(),
                };

                nums.push(num);
            }
            format!("{}{}", nums[0], nums[nums.len() - 1])
                .parse::<usize>()
                .unwrap()
        })
        .sum();
    println!("p2 sum {:?}", p2);
}
