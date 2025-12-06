from typing import Tuple

## Main function
# Parses the file, extracts the operators and reads the values (either vertical or horizontal read)
# Then applies the operators to the values, and prints the sum
def execute():
    matrix = parse_file("real_input.txt")
    operators = parse_vertically(matrix[-1])

    values_vertical = [parse_vertically(x) for x in matrix[:-1]]
    values_vertical = transpose(values_vertical)
    first_results = compute_results(values_vertical, operators)
    print(sum(first_results))

    values_horizontal = parse_horizontally(matrix[:-1])
    second_results = compute_results(values_horizontal, operators)
    print(sum(second_results))

# Parses the values in normal reading direction, while removing the blanks
def parse_vertically(s: str) -> list[str]:
    split = s.split(' ')
    res = [x for x in split if x != '']
    return res

# Transposes a matrix
# This is used for values read vertically, since they are still grouped horizontally
def transpose(mat: list[list[str]]) -> list[list[str]]:
    n = len(mat)
    m = len(mat[0])
    res = [[mat[i][j] for i in range(n)] for j in range(m)]
    return res

# Reads the values horizontally (from top to bottom)
# When a column if completely empty, we know this starts a new set of values
def parse_horizontally(mat: list[str]) -> list[list[str]]:
    n = len(mat)
    m = len(mat[0])
    res = []
    current_group = []
    for j in range(m):
        val = ''
        for i in range(n):
            x = mat[i][j]
            if x != ' ':
                val += x
        if val == '':
            res.append(current_group)
            current_group = []
        else:
            current_group.append(val)
    res.append(current_group)
    return res

# Given a list of operators and for each one, a list of values
# Applies the operator to the values, and return the list of results
def compute_results(values: list[list[str]], operators: list[str]) -> list[int]:
    n = len(operators)
    res = []
    for i in range(n):
        op = operators[i]
        if op == '+':
            total = 0
        elif op == '*':
            total = 1
        for val in values[i]:
            if op == '+':
                total += int(val)
            elif op == '*':
                total *= int(val)
        res.append(total)
    return res

    
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