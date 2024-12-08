def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

STEPS = 380

def solve_part_1():
    buffer = [0]
    ptr = 0
    for i in range(1, 2018):
        ptr = (ptr + STEPS) % len(buffer) + 1
        buffer.insert(ptr, i)
    return buffer[(buffer.index(2017) + 1) % 2018]

def solve_part_2():
    zero_index = 0
    before_count = 0
    after_count = 0
    ptr = 0
    buffer_length = 1

    element = 1 # 1 is always inserted to in-front of 0 in the circular buffer
    for i in range(1, 50_000_001):
        ptr = (ptr + STEPS) % buffer_length + 1
        if ptr == zero_index + 1:
            element = i
        if ptr <= zero_index:
            before_count += 1
            zero_index += 1
        else:
            after_count += 1
        buffer_length += 1

    return element
    
print(solve_part_2())
