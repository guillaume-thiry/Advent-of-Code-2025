from typing import Tuple

## Main function
# Parse the file into intervals and ids to test. Sort the intervals by their start.
# Then computes both results using the corresponding auxiliary functions.
def execute():
    intervals, ids = parse_file("real_input.txt") 
    intervals.sort(key = lambda x: x[0])
    count_fresh = 0
    for i in ids:
        if is_in_interval(i, intervals):
            count_fresh += 1
    total_interval_length = measure_intervals(intervals)
    print(count_fresh)
    print(total_interval_length)

# Given a list of intervals sorted by start, check if an id belongs to one of them
# Intervals strictly before are skipped. Return early once we reach intervals strictly after.
def is_in_interval(id: int, intervals: list[tuple[int, int]]) -> bool:
    for a,b in intervals:
        if b<id:
            continue
        if a>id:
            return False
        return True
    return False

# Given a list of intervals sorted by start, computes the total span of all intervals
# This is done by merging overlapping intervals (end_i+1<=start_i)
# And adding to the count the length of the uniquely merged intervals
def measure_intervals(intervals: list[tuple[int, int]]) -> int:
    res = 0
    start, end = intervals[0]
    i = 1
    while(i<len(intervals)):
        if intervals[i][0]<=end:
            end = max(end, intervals[i][1])
        else:
            res += (end-start+1)
            start, end = intervals[i]
        i += 1
    res += (end-start+1)
    return res
    
# Parses the input file into a list of intervals and values to test
def parse_file(file_name: str) -> tuple[list[tuple[int, int]], list[int]]:
    intervals = []
    ids = []
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip('\n')
            if line == '':
                continue
            split = line.split('-')
            if len(split)==2:
                intervals.append((int(split[0]), int(split[1])))
            else:
                ids.append(int(split[0]))
    return intervals, ids

if __name__ == "__main__":
    execute()