from typing import Tuple, Dict

## Main function
# 
def execute():
    shapes, regions = parse_file("real_input.txt")
    count_trivial_fit = 0
    count_trivial_no_fit = 0
    count_unclear = 0
    for region, needed in regions:
        size = region[0]*region[1]
        fit = trivial_fit(size, needed, shapes)
        if fit == "yes":
            count_trivial_fit += 1
        elif fit == "no":
            count_trivial_no_fit += 1
        else:
            count_unclear += 1
    print("Trivial fit:", count_trivial_fit)
    print("Trivial no fit:", count_trivial_no_fit)
    print("Unclear:", count_unclear)

    
def trivial_fit(region_size: int, needed: list[int], shapes: list[int]) -> str:
    rough_size = 9*sum(needed)
    correct_size = 0
    for i in range(len(needed)):
        correct_size += needed[i]*shapes[i]
    if rough_size<=region_size:
        return "yes"
    if correct_size>region_size:
        return "no"
    return "maybe"


# Parses the input file into
def parse_file(file_name: str) -> tuple[list[int], list[tuple[list[int], list[int]]]]:
    shape_size = 0
    shapes = []
    regions = []
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip('\n')
            if len(line) == 2:
                continue
            if len(line) == 3:
                for i in range(3):
                    shape_size += int(line[i] == '#')
                continue
            if len(line) == 0:
                shapes.append(shape_size)
                shape_size = 0
                continue
            split = line.split(':')
            dims = split[0].split('x')
            dims = [int(x) for x in dims]
            needed = split[1][1:].split(' ')
            needed = [int(x) for x in needed]
            regions.append((dims, needed))
    return (shapes, regions)

    
    return res

if __name__ == "__main__":
    execute()