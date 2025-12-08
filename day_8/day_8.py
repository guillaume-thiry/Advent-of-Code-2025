from typing import Tuple
import heapq

## Class to implement the union-find algorithm
# Textbook union-find, not optimized
class UnionFind:
    def __init__(self, n: int):
        self.parents = [i for i in range(n)]
        self.sizes = [1 for i in range(n)]

    def find(self, i: int) -> int:
        while(self.parents[i]!=i):
            i = self.parents[i]
        return i
    
    def union(self, i:int, j:int):
        pi = self.find(i)
        pj = self.find(j)
        if pi != pj:
            self.parents[pi]=pj
            self.sizes[pj] += self.sizes[pi]
    
    def get_size(self, i: int) -> int:
        pi = self.find(i)
        return self.sizes[pi]

    def get_cluster_sizes(self) -> list[int]:
        sizes = []
        seen = set()
        for i in range(len(self.parents)):
            pi = self.find(i)
            if pi not in seen:
                sizes.append(self.sizes[pi])
                seen.add(pi)
        return sizes

## Main function 1
# Parses the values, and find the N shortest connections
# Applies them with the union-find algorithm to keep track of the clusters created
# Gets the sizes of the clusters and find the three largest for the final result
def execute_1():
    values = parse_file("real_input.txt")
    connections = find_n_shortest_distances(values, 1000)
    n = len(values)
    uf = UnionFind(n)
    for i,j in connections:
        uf.union(i,j)
    sizes = uf.get_cluster_sizes()
    sizes.sort(reverse=True)
    print(sizes[0]*sizes[1]*sizes[2])

## Main function 2
# Parses the values and computes all distances sorted
# Applies the union-find on the connections, one by one (from shortest to longest)
# Stops when the formed cluster is of maximal size (i.e there is only one cluster)
# Computes the corresponding result, based on the last connection made
def execute_2():
    values = parse_file("real_input.txt")
    connections = find_all_distances_sorted(values)
    n = len(values)
    uf = UnionFind(n)
    while(True):
        i, j = connections.pop()
        uf.union(i, j)
        if uf.get_size(i) == n:
            break
    print(values[i][0]*values[j][0])

# Computes the Euclidean distance in 3 dimensions
def compute_distance(a: list[int], b: list[int]) -> int:
    dx = (a[0]-b[0])**2
    dy = (a[1]-b[1])**2
    dz = (a[2]-b[2])**2
    d = (dx+dy+dz)**0.5
    return int(d)

# Computes all the possible distances and keep the n shortest using a heap structure
# At every time, the heap contains the shortest distances found so far
# When the heap becomes too large, we pop the largest value from it as it cannot be in the final result
# Returns only the pairs of indices based on the shortest distances
def find_n_shortest_distances(values: list[list[int]], n: int) -> list[tuple[int, int]]:
    h = []
    heapq.heapify(h)
    l = len(values)
    for i in range(l):
        for j in range(i+1,l):
            dist = compute_distance(values[i], values[j])
            heapq.heappush(h, (-dist, (i,j)))
            if len(h)>n:
                heapq.heappop(h)
    res = [b for _,b in h]
    return res

# Computes all the possible distances and sorts them
# Returns only the pairs of indices, keeping the distance-based sorting
def find_all_distances_sorted(values: list[list[int]]) -> list[tuple[int, int]]:
    distances = []
    n = len(values)
    for i in range(n):
        for j in range(i+1, n):
            dist = compute_distance(values[i], values[j])
            distances.append((dist, (i,j)))
    distances.sort(key = lambda x: -x[0])
    res = [b for _,b in distances]
    return res
    
# Parses the input file into a list of values
def parse_file(file_name: str) -> list[list[int]]:
    res = []
    with open(file_name, 'r') as file:
        for line in file:
            values = line.strip('\n').split(',')
            res.append([int(x) for x in values])
    return res

if __name__ == "__main__":
    execute_1()
    execute_2()