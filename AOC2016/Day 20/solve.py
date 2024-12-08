def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    blocked_ranges = []
    for line in read_input_file_data().splitlines():
        blocked_ranges.append(tuple(map(int, line.split('-'))))
    blocked_ranges.sort()

    START = 0
    END = 4294967295
    end_block = blocked_ranges[0][0]
    if end_block != START:
        return START
    
    for l, r in blocked_ranges:
        if l > end_block + 1:
            return end_block + 1
        else:
            end_block = max(end_block, r)
    return end_block + 1

def solve_part_2():
    blocked_ranges = []
    for line in read_input_file_data().splitlines():
        blocked_ranges.append(tuple(map(int, line.split('-'))))
    blocked_ranges.sort()

    START = 0
    END = 4294967295
    end_block = blocked_ranges[0][0]
    count_allowed = 0
    if end_block != START:
        count_allowed += end_block - START
    for l, r in blocked_ranges:
        if l > end_block + 1:
            count_allowed += l - (end_block + 1)
        end_block = max(end_block, r)
    count_allowed += (END + 1) - (end_block + 1)
    return count_allowed
    
print(solve_part_2())
