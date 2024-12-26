def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    def is_lock(scheme):
        return scheme[0][0] == '#'
    def is_key(scheme):
        return scheme[0][0] == '.'
    def parse_lock(lock_scheme):
        lock = [0] * 5
        for i in range(5):
            for x in range(5, -1, -1):
                if lock_scheme[x][i] == '#':
                    lock[i] = x
                    break
            else:
                raise Exception("Not found")
        return tuple(lock)
    def parse_key(key_scheme):
        key = [0] * 5
        for i in range(5):
            for x in range(1, 7):
                if key_scheme[x][i] == '#':
                    key[i] = 5-(x-1)
                    break
            else:
                raise Exception("Not found")
        return tuple(key)
    
    schemes = list(map(lambda s: s.splitlines(), read_input_file_data().split('\n\n')))
    locks = [parse_lock(lock) for lock in list(filter(is_lock, schemes))]
    keys = [parse_key(key) for key in list(filter(is_key, schemes))]
    
    fits = 0
    for lock in locks:
        for key in keys:
            for i in range(5):
                if lock[i] + key[i] > 5:
                    break
            else:
                fits += 1
    return fits

def solve_part_2():
    pass
    
print(solve_part_1())
