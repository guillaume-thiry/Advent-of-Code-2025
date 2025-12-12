from typing import Tuple

## Main function
# Computes the result and print it
def execute():
    coordinates = parse_file("real_input.txt")
    res = find_max_area(coordinates)
    print(res)

# Goes through all the pairs of corners, and computes the area
# For part 2 only, also checks if the rectangle is eligible
# Finds the max area for all eligible rectangles
def find_max_area(coordinates: list[tuple[int, int]]) -> int:
    n = len(coordinates)
    max_area = 0
    for i in range(n):
        for j in range(i+1,n):
            # Only for part 2
            if not is_valid(i, j, coordinates):
                continue
            a,b = coordinates[i]
            c,d = coordinates[j]
            area = (abs(a-c)+1)*(abs(b-d)+1)
            max_area = max(max_area, area)
    return max_area

# Checks if a rectangle is eligible, that is:
# * No other point of the input is strictly inside (allowed on the border)
# * A line connecting to neighbor points do not cross the rectangle
# The second one is done by computing the middle of the line, and checking if it is inside the rectangle
def is_valid(i: int, j:int, coordinates: list[tuple[int, int]]):
    n = len(coordinates)
    pi = coordinates[i]
    pj = coordinates[j]
    for k in range(n):
        if k==i or k==j:
            continue
        pk = coordinates[k]
        if is_inside(pi, pj, pk):
            return False
        k2 = (k+1)%n
        if k2==i or k2==j:
            continue
        pk2 = coordinates[k2]
        mid = middle(pk, pk2)
        if is_inside(pi, pj, mid):
            return False
    return True
               
# Given a rectangle described by 2 points, checks if a third point is stricly inside
def is_inside(pi: tuple[int, int], pj: tuple[int, int], pk: tuple[int, int]) -> bool:
    if (pi[0]<pk[0] and pk[0]<pj[0]) or (pj[0]<pk[0] and pk[0]<pi[0]):
        if (pi[1]<pk[1] and pk[1]<pj[1]) or (pj[1]<pk[1] and pk[1]<pi[1]):
            return True
    return False

# Given 2 points, finds the middle of the connecting line
def middle(pa: tuple[int, int], pb: tuple[int, int]) -> tuple[int, int]:
    x = int((pa[0]+pb[0])/2)
    y = int((pa[1]+pb[1])/2)
    return (x,y)

# Parses the input file into list of coordinates
def parse_file(file_name: str) -> list[tuple[int, int]]:
    res = []
    with open(file_name, 'r') as file:
        for line in file:
            values = line.strip('\n').split(',')
            res.append((int(values[0]),int(values[1])))
    return res

if __name__ == "__main__":
    execute()