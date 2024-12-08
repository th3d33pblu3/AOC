from functools import reduce

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def knot_hash(key) -> str:
    SIZE = 256
    ROUNDS = 64
    lengths = list(map(ord, key))
    lengths.extend([17, 31, 73, 47, 23])
    nums = [i for i in range(SIZE)]

    def reverse_range(start, end):
        nums_copy = nums.copy()
        true_end = end % SIZE
        i = start % SIZE
        j = (end - 1) % SIZE
        while i != true_end:
            nums[i] = nums_copy[j]
            i = (i + 1) % SIZE
            j = (j - 1 + SIZE) % SIZE

    current_pos = 0
    skip_size = 0
    for _ in range(ROUNDS):
        for length in lengths:
            start, end = current_pos, current_pos + length
            reverse_range(start, end)
            current_pos = (current_pos + length + skip_size) % SIZE
            skip_size = (skip_size + 1) % SIZE

    hash = ""
    for block_num in range(len(nums) // 16):
        block = nums[block_num * 16 : (block_num + 1) * 16]
        hex_val = hex(reduce(lambda a, b: a ^ b, block))[2:]
        if len(hex_val) < 2:
            hex_val = "0" + hex_val
        hash += hex_val
    assert len(hash) == 32
    return hash

def solve_part_1():
    key_string = read_input_file_data()
    used = 0
    for i in range(128):
        key = f"{key_string}-{i}"
        hash = knot_hash(key)
        used += bin(int(hash, 16))[2:].count('1')
    return used

def solve_part_2():
    SIZE = 128
    key_string = read_input_file_data()
    layout = [[b == '1' for b in bin(int(knot_hash(f"{key_string}-{i}"), 16))[2:].zfill(SIZE)] for i in range(SIZE)]
    tracker = [[False] * SIZE for _ in range(SIZE)]

    region = 0
    for r in range(SIZE):
        for c in range(SIZE):
            if tracker[r][c] or not layout[r][c]: # ignore tracked or free
                continue
            region += 1
            frontier = {(r, c)}
            while not frontier == set():
                new_frontier = set()
                for i, j in frontier:
                    if tracker[i][j]: # ignore tracked
                        continue
                    tracker[i][j] = True # track current grid
                    if not layout[i][j]: # ignore free
                        continue
                    # expand used
                    if i - 1 >= 0:
                        new_frontier.add((i-1, j))
                    if i + 1 < SIZE:
                        new_frontier.add((i+1, j))
                    if j - 1 >= 0:
                        new_frontier.add((i, j-1))
                    if j + 1 < SIZE:
                        new_frontier.add((i, j+1))
                frontier = new_frontier
    return region
    
print(solve_part_2())
