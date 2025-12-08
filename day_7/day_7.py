from typing import Tuple

## Main function
# 
def execute():
    lines = parse_file("real_input.txt")
    current = init_start(lines[0])
    total = 0
    for line in lines[1:]:
        current, splits = compute_next_line(current, line)
        total += splits
    print("First result:", total)
    print("Second result:", sum(current))

def init_start(s: str) -> list[int]:
    split = s.split('S')
    assert len(split) == 2
    res = ([0] * len(split[0])) + [1] + ([0] * len(split[1]))
    return res

def compute_next_line(current: list[int], line: str) -> tuple[list[int], int]:
    n = len(current)
    count_splits = 0
    next = [0] * n
    for i in range(n):
        if not current[i]:
            continue
        if line[i] == '^':
            next[i-1]+= current[i]
            next[i+1]+= current[i]
            count_splits += 1
        else:
            next[i]+= current[i]
    return (next, count_splits)

    

    
# Parses the input file into a list of lines
# Further parsing (vertical or horizontal) is done later
def parse_file(file_name: str) -> list[str]:
    res = []
    with open(file_name, 'r') as file:
        for line in file:
            res.append(line.strip('\n'))
    return res

if __name__ == "__main__":
    execute()