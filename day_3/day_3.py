from typing import Tuple

## Main function
# Parse the banks in the file, computes their max power and sums them
def execute():
    banks = parse_file("real_input.txt")
    res = 0
    for bank in banks:
        res += max_power_n(bank, 12)
    print(res)

# Computes the max power of a bank using 2 batteries
# This is done by storing the partial maximum (from index till the end) for the unit number
def max_power_2(bank: str) -> int:
    l = len(bank)
    max_10 = 0
    max_10_id = -1
    max_1 = 0
    partial_max = [0]*(l-1)
    for i in range(l-2, -1, -1):
        if int(bank[i]) >= max_10:
            max_10 = int(bank[i])
            max_10_id = i
        max_1 = max(max_1, int(bank[i+1]))
        partial_max[i] = max_1
    res = 10 * max_10 + partial_max[max_10_id]
    return res 

# Computes the max power of a bank using n batteries
# For each iteration, the partial maximum (index till end) for a power of ten is calculated
# Using the value at index and the previous partial maximum (for the previous power of ten)
def max_power_n(bank: str, n: int) -> int:
    l = len(bank)
    partial_max = [0]*(l+1)
    multi = 1
    for i in range(n):
        new_partial_max = [0]*(l-i-1)
        max_after = 0
        for j in range(l-i-1, -1, -1):
            candidate = int(bank[j]) * multi + partial_max[j]
            max_after = max(max_after, candidate)
            if j>0:
                new_partial_max[j-1] = max_after
        partial_max = new_partial_max
        multi *= 10
    return max_after

    
# Parses the input file into a list of banks
def parse_file(file_name: str) -> list[str]:
    res = []
    with open(file_name, 'r') as file:
        for line in file:
            res.append(line.strip('\n'))
    return res

if __name__ == "__main__":
    execute()