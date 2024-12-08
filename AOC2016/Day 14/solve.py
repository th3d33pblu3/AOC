from hashlib import md5

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

SALT = read_input_file_data()

def get_first_triple(h):
    buff = h[0]
    count = 1
    for c in h[1:]:
        if c == buff:
            count += 1
            if count == 3:
                return c
        else:
            buff = c
            count = 1
    return None

def get_penta(h):
    chars = set()
    for c in "0123456789abcdef":
        if c * 5 in h:
            chars.add(c)
    return chars

def get_hash_info(n):
    hash = md5((SALT + str(n)).encode()).digest().hex()
    return (get_first_triple(hash), get_penta(hash))

def solve_part_1():
    i = -1
    keys = []
    num_keys = 0

    def get_triple_penta(index):
        if index >= len(keys):
            for x in range(len(keys), index + 1):
                keys.append(get_hash_info(x))
        return keys[index]

    while num_keys < 64:
        i += 1
        triple, penta = get_triple_penta(i)
        if triple == None:
            continue
        for index in range(i + 1, i + 1000 + 1):
            new_t, new_p = get_triple_penta(index)
            if triple in new_p:
                num_keys += 1
                break
    return i

def get_stretched_hash_info(n):
    hash = md5((SALT + str(n)).encode()).digest().hex()
    for _ in range(2016):
        hash = md5(hash.encode()).digest().hex()
    return (get_first_triple(hash), get_penta(hash))

def solve_part_2():
    i = -1
    keys = []
    num_keys = 0

    def get_triple_penta(index):
        if index >= len(keys):
            for x in range(len(keys), index + 1):
                keys.append(get_stretched_hash_info(x))
        return keys[index]

    while num_keys < 64:
        i += 1
        triple, penta = get_triple_penta(i)
        if triple == None:
            continue
        for index in range(i + 1, i + 1000 + 1):
            new_t, new_p = get_triple_penta(index)
            if triple in new_p:
                num_keys += 1
                break
    return i

print(solve_part_2())
