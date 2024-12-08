from collections import Counter

def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

def solve_part_1():
    file = read_input_file()
    valid_count = 0
    for line in file.read().splitlines():
        words = line.split()
        word_counter = Counter(words)
        if word_counter.most_common(1)[0][1] == 1:
            valid_count += 1

    return valid_count

def solve_part_2():
    file = read_input_file()
    valid_count = 0
    for line in file.read().splitlines():
        words = line.split()
        counters = []
        for word in words:
            counters.append(Counter(word))
        increment = 1
        for i in range(len(counters)):
            current = counters[i]
            remaining = counters[i + 1:]
            for counter in remaining:
                if current == counter:
                    increment = 0
        valid_count += increment

    return valid_count
    
print(solve_part_2())
