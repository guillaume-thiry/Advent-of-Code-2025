from typing import Tuple

## Main function
# Reads the input file, parses it into instructions and executes them
# Both counts are updated after each executed instruction
def execute():
    instructions = parse_file("input1.txt")
    x = 50
    exact_counter = 0
    partial_counter = 0
    for instruction in instructions:
        x, y = execute_instruction(x, instruction)
        if x==0:
            exact_counter += 1
        partial_counter += y
    print("The arrow stopped exactly on 0:", exact_counter, "times")
    print("The arrow went over 0:", partial_counter, "times")

# Parses a line in the input file           
def parse_line(line: str) -> tuple[str, int]:
    dir = line[0]
    if dir!='R' and dir!='L':
        raise Exception("Direction not known")
    length = int(line[1:])
    return(dir, length)

# Parses the input line
def parse_file(file_name: str) -> list[tuple[str, int]]:
    res = []
    with open(file_name, 'r') as file:
        for line in file:
            res.append(parse_line(line))
    return res

# Given an initial position and an instruction, computes the next position
# Based on the instruction, also computes the number of times passing over 0 without stopping 
def execute_instruction(x: int, instruction: tuple[str, int]) -> tuple[int, int]:
    dir, length = instruction
    if dir=='R':
        new_x = x + length
    elif dir=='L':
        new_x = x - length
    else:
        raise Exception("Unknown instruction")
    if new_x>0:
        y = new_x//100
    else:
        y = abs((new_x-1)//100)
        if x==0:
            y -= 1
    return new_x%100, y

if __name__ == "__main__":
    execute()