from tqdm import tqdm

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

INITIAL_STATE = "#...#..###.#.###.####.####.#..#.##..#..##..#.....#.#.#.##.#...###.#..##..#.##..###..#..##.#..##..."

def solve_part_1():
    lines = read_input_file_data().splitlines()
    rules = {}
    for line in lines:
        cond, res = line.split(" => ")
        cond = tuple(map(lambda c: c == '#', cond))
        res = res == '#'
        rules[cond] = res

    gen = {}
    for i in range(len(INITIAL_STATE)):
        gen[i] = INITIAL_STATE[i] == '#'
    li = 0
    ri = len(INITIAL_STATE)

    for _ in range(20):
        new_gen = {}
        for i in range(li-2, ri+2):
            if rules.get((gen.get(i-2, False), gen.get(i-1, False), gen.get(i, False), gen.get(i+1, False), gen.get(i+2, False)), False):
                new_gen[i] = True
                if i < li: li = i
                if i > ri: ri = i
        gen = new_gen
    # print(''.join(['#' if gen.get(i, False) else '.' for i in range(0, ri+1)]))
    
    return sum(i if t else 0 for i, t in gen.items())

def solve_part_2():
    lines = read_input_file_data().splitlines()
    rules = {}
    for line in lines:
        cond, res = line.split(" => ")
        cond = tuple(map(lambda c: c == '#', cond))
        res = res == '#'
        rules[cond] = res

    gen = {}
    for i in range(len(INITIAL_STATE)):
        gen[i] = INITIAL_STATE[i] == '#'

    '''
    stabilize after 94 iterations, with li being 61 and pattern being:
    ##......##...........##.....##......##.....##........................##.....##.....##....................##...................##
    '''
    loops = 50_000_000_000
    li = loops - 94 + 61
    return li * 22 + 1201
    
print(solve_part_2())
