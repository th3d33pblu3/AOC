from collections import Counter

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    data = read_input_file_data()
    twos = 0
    threes = 0
    for box in data.splitlines():
        counter = Counter(box)
        for count in counter.values():
            if count == 2:
                twos += 1
                break
        for count in counter.values():
            if count == 3:
                threes += 1
                break
    return twos * threes

def solve_part_2():
    possible_collisions = set()
    for box in read_input_file_data().splitlines():
        for i in range(len(box)):
            left = box[:i]
            right = box[i + 1:]
            box_str = left + str(i) + right
            if box_str in possible_collisions:
                return left + right
            else:
                possible_collisions.add(box_str)
    
print(solve_part_2())
