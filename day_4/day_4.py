from typing import Tuple

## Main function
# 
def execute():
    grid = parse_file("real_input.txt")
    #res = remove_rolls_basic(grid)
    res = remove_rolls_advanced(grid)
    print(res)
    
POSITIONS = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def count_neighbors(grid: list[list[str]], i: int, j:int) -> int:
    n = len(grid)
    m = len(grid[0])
    neighbors = 0
    for di,dj in POSITIONS:
        if (i+di<0) or (i+di==n) or (j+dj<0) or (j+dj==m):
            continue
        if grid[i+di][j+dj]!='.':
            neighbors += 1
    return neighbors

def remove_rolls_basic(grid: list[list[str]]) -> int:
    n = len(grid)
    m = len(grid[0])
    res = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j]=='.':
                continue
            if count_neighbors(grid, i, j)<4:
                res += 1
    return res

def remove_rolls_advanced(grid: list[list[str]]) -> int:
    n = len(grid)
    m = len(grid[0])
    rolls_to_remove = []
    # Initialization
    for i in range(n):
        for j in range(m):
            if grid[i][j]=='@':
                grid[i][j] = count_neighbors(grid, i, j)
                if grid[i][j] < 4:
                    rolls_to_remove.append((i,j))
    res = 0
    while(len(rolls_to_remove)>0):
        x,y = rolls_to_remove.pop()
        res += 1
        next_to_remove = remove_one_roll(grid, x, y)
        rolls_to_remove += next_to_remove
    return res

def remove_one_roll(grid: list[list[str]], i: int, j:int) -> list[tuple[int, int]]:
    n = len(grid)
    m = len(grid[0])
    next_to_remove = []
    for di,dj in POSITIONS:
        if (i+di<0) or (i+di==n) or (j+dj<0) or (j+dj==m):
            continue
        if grid[i+di][j+dj]!='.':
            grid[i+di][j+dj]-=1
            if grid[i+di][j+dj]==3:
                next_to_remove.append((i+di,j+dj))
    return next_to_remove
    
# Parses the input file into a list of banks
def parse_file(file_name: str) -> list[list[str]]:
    res = []
    with open(file_name, 'r') as file:
        for line in file:
            line_res = []
            for c in line.strip('\n'):
                line_res.append(c)
            res.append(line_res)
    return res

if __name__ == "__main__":
    execute()