from typing import Tuple

## Main function
# Parses the ranges from the input file, and find all invalid IDs for each range
# Adds up the invalid IDs together
def execute():
    ranges = parse_file("real_input.txt")
    total = 0
    for i,j in ranges:
        invalids = find_invalids(i, j)
        for x in invalids:
            total += x
    print(total)

# Browses all values in a range and keeps the invalid ones given the selection function
def find_invalids(start_range: int, end_range: int) -> list[int]:
    return [x for x in range(start_range, end_range+1) if is_invalid_bis(x)]  # Use either is_invalid() or is_invalid_bis()

## First selection function for the first task
# Splits the ID in two parts and compare them
def is_invalid(x: int) -> bool:
    y = str(x)
    l = len(y)
    if l%2:
        return False
    a = y[:(l//2)]
    b = y[(l//2):]
    return a==b

## Second selection function for the second task
# For each possible size of split, check if splitting the string makes it invalid 
def is_invalid_bis(x:int) -> bool:
    y = str(x)
    l = len(y)
    for i in range(1,l):
        if is_invalid_split(y, i):
            return True
    return False

# Splits the string using the provided size, and compare if all splits are equal
def is_invalid_split(string: str, l) -> bool:
    if len(string)%l!=0:
        return False
    ref_substring = string[0:l]
    i = l
    while(i<len(string)):
        substring = string[i:i+l]
        if substring != ref_substring:
            return False
        i += l
    return True
    
# Parses the input file into a list of splits (start, end)
def parse_file(file_name: str) -> list[tuple[int, int]]:
    res = []
    with open(file_name, 'r') as file:
        content = file.read()
        ranges = content.split(',')
        for r in ranges:
            split_range = r.split('-')
            assert(len(split_range)==2)
            res.append((int(split_range[0]), int(split_range[1])))
    return res

if __name__ == "__main__":
    execute()