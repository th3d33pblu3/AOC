from collections import Counter

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    l, r = zip(*[tuple(map(lambda x: int(x), line.split("   "))) for line in read_input_file_data().splitlines()])
    l = list(l)
    r = list(r)
    l.sort()
    r.sort()

    dist = 0
    for i in range(len(l)):
        dist += abs(l[i] - r[i])
    return dist

def solve_part_2():
    l, r = zip(*[tuple(map(lambda x: int(x), line.split("   "))) for line in read_input_file_data().splitlines()])
    l = list(l)
    r = Counter(r)

    sim = 0
    for i in l:
        sim += r[i] * i
    return sim
    
print(solve_part_2())
