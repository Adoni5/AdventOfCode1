from collections import deque
from support import get_input

test_input = """bvwbjplbgvbhsrlpgdmjqwftvncz
nppdvjthqldpwncqszvftbrmjlhg
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"""

def call_on_me(signal_str: str, marker_len: int = 4) -> int:
    """Process a signal string and return the index (1 based) where the signal is found"""
    line = signal_str.strip()
    signal = deque(maxlen=marker_len)
    for i, signal_ch in enumerate(line):
        signal.append(signal_ch)
        if len(set(signal)) == marker_len:
            return (i + 1)

if __name__ == "__main__":
    # test
    for line in test_input.splitlines():
        print(call_on_me(line))
        print(f"p2 {call_on_me(line, marker_len=14)}")

    # real
    input = get_input("6")
    # p1
    print(call_on_me(input))
    # p2
    print(call_on_me(input, marker_len=14))