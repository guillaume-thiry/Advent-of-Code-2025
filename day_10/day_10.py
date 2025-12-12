from typing import Tuple
from scipy.optimize import linprog

## Main function
# Computes both results and prints them
def execute():
    input = parse_file("real_input.txt")
    a = 0
    b = 0
    for lights, buttons, joltages in input:
        a += find_minimum(lights, buttons)
        b += solve_equation(buttons, joltages)
    print(a)
    print(b)

# For the first task, each button can be pressed either 0 or 1 time
# So we explore each path by going through the buttons and choosing both options
# This is done through an auxiliary function, that also keeps the number of buttons pressed so far
# Whenever a path leads to the result sequence of light, checks the number of buttons against the current min
# Note: we actually start from the end sequence, and try to turn all lights off
# This is because checking for this sequence (all off) is quite easy to do (sum == 0)
def find_minimum(lights: list[int], buttons: list[list[int]]) -> int:
    minimum = len(buttons)

    def aux(lights: list[int], pos: int, pressed: int, buttons: list[list[int]]):
        nonlocal minimum
        if sum(lights)==0:
            minimum = min(minimum, pressed)
            return
        n = len(buttons)
        if pos==n:
            return
        # Path 1: Do not press current button
        aux(lights, pos+1, pressed, buttons)
        # Path 2: Press current button
        button = buttons[pos]
        apply(lights, button)
        aux(lights, pos+1, pressed+1, buttons)
        # Cancel action for backtracking
        apply(lights, button)
    
    aux(lights, 0, 0, buttons)
    return minimum

# For the second task, we solve the linear equation using an external lib
def solve_equation(buttons: list[list[int]], joltages: list[int]) -> int:
    coeff = [1 for _ in range(len(buttons))]
    A = [[int(i in b) for b in buttons] for i in range(len(joltages))]
    res = linprog(coeff, A_eq=A, b_eq=joltages, integrality=1).fun
    return int(res)

# Given lights and a pressed button, applies the changes to the lights in place
def apply(lights: list[int], button: list[int]):
    for b in button:
        lights[b] = (lights[b]+1)%2
    
# Parses the input file into a list of (lights, buttons, joltages)
def parse_file(file_name: str) -> list[tuple[list[int], list[list[int]]], list[int]]:
    res = []
    with open(file_name, 'r') as file:
        for line in file:
            splits = line.strip('\n').split(' ')
            lights = []
            for i in range(1, len(splits[0])-1):
                x = splits[0][i]
                if x == '.':
                    lights.append(0)
                else:
                    lights.append(1)
            buttons = []
            for s in splits[1:-1]:
                b = []
                vals = s[1:-1].split(',')
                for v in vals:
                    b.append(int(v))
                buttons.append(b)
            joltages = []
            for v in splits[-1][1:-1].split(','):
                joltages.append(int(v))
            res.append((lights, buttons, joltages))
    return res

if __name__ == "__main__":
    execute()