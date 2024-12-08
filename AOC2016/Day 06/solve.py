from collections import Counter

def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

def solve_part_1():
    NUM_LETTERS = 8
    counters = []
    for _ in range(NUM_LETTERS):
        counters.append(Counter())
    file = read_input_file()
    for word in file.read().splitlines():
        for i in range(len(word)):
            counter = counters[i]
            char = word[i]
            counter.update(char)
    output = ""
    for counter in counters:
        output += counter.most_common()[0][0]
    return output

def solve_part_2():
    NUM_LETTERS = 8
    counters = []
    for _ in range(NUM_LETTERS):
        counters.append(Counter())
    file = read_input_file()
    for word in file.read().splitlines():
        for i in range(len(word)):
            counter = counters[i]
            char = word[i]
            counter.update(char)
    output = ""
    for counter in counters:
        output += counter.most_common()[-1][0]
    return output
    
print(solve_part_2())
