from typing import Tuple, Dict

## Main function
# Computes both results and prints them
def execute():
    graph = parse_file("real_input.txt")
    seen = {}
    res_1 = explore_1('you', graph, seen)
    seen.clear()
    res_2 = explore_2('svr', graph, seen)
    print(res_1)
    print(res_2[2])

# Explore all paths of the graph using a DFS
# When all paths from a node to the end have been explored, we store the result for this node is a map
# So that if we find again this node later in the DFS, we already know how many different paths reach the end
# To find the number of paths from a node, we try each of its neighbors and add the number of paths 
def explore_1(node: str, graph: dict[str, list[str]], seen: dict[str, int]) -> int:
    if node == 'out':
        return 1
    if node in seen:
        return seen[node]
    res = 0
    for neighbor in graph[node]:
        res += explore_1(neighbor, graph, seen)
    seen[node] = res
    return res

# Explore all paths of the graph using a DFS, similarly as before
# The twist is that we keep 3 values for a node:
# * Number of paths from node to end, with [0 OR 1 OR 2] of the 2 required nodes
# If the node is one of the 2 we need to find, values in the vector shift right
# The graph is acyclic, so the case of seeing twice the same node of interest is not possible
# That way, it is enough to check that we have found 2 nodes of interest in the path
def explore_2(node: str, graph: dict[str, list[str]], seen: dict[str, list[int]]) -> list[int]:
    if node == 'out':
        return [1,0,0]
    if node in seen:
        return seen[node]
    res = [0,0,0]
    for neighbor in graph[node]:
        add = explore_2(neighbor, graph, seen)
        for i in range(3):
            res[i] += add[i]
    if node in ['dac', 'fft']:
        res[2] = res[1]
        res[1] = res[0]
        res[0] = 0
    seen[node] = res
    return res
    

# Parses the input file into a map
# node -> list of neighbors
def parse_file(file_name: str) -> dict[str, list[str]]:
    res = {}
    with open(file_name, 'r') as file:
        for line in file:
            split = line.strip('\n').split(':')
            neighbors = split[1][1:].split(' ')
            res[split[0]] = neighbors
    return res

if __name__ == "__main__":
    execute()