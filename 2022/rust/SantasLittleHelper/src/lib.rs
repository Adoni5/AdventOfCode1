use dotenvy::from_path;
use reqwest::header;
use std::env;

fn _return_headers() -> reqwest::header::HeaderMap {
    from_path("../.env").unwrap();

    let session = env::var("SESSION").unwrap();
    let cookie = format!("session={}", session);
    let mut headers = header::HeaderMap::new();
    headers.insert(
        "cookie",
        header::HeaderValue::from_str(cookie.as_str()).unwrap(),
    );
    headers
}

pub fn get_input(day: &str) -> String {
    let headers = _return_headers();
    let client = reqwest::blocking::Client::builder()
        .user_agent("roryjmunro1@gmail.com, learning rust with AoC, (Thanks Eric)")
        .default_headers(headers)
        .build()
        .unwrap();
    client
        .get(format!("https://adventofcode.com/2022/day/{day}/input"))
        .send()
        .unwrap()
        .text()
        .unwrap()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn open_env() {
        from_path("../.env").unwrap();
        env::var("SESSION").unwrap();
    }

    #[test]
    fn test_headers() {
        _return_headers();
    }
}
