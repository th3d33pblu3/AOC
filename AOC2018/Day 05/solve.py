import string

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def is_polar(c: str, d: str) -> bool:
    if str.islower(c):
        return c.upper() == d
    return c.lower() == d

def solve_part_1():
    lst = [c for c in read_input_file_data()]
    size = len(lst)
    i = 0
    while i < size - 1:
        c = lst[i]
        d = lst[i + 1]
        if is_polar(c, d):
            lst.pop(i + 1) # remove d
            lst.pop(i)     # remove c
            size -= 2
            i -= 1 if i != 0 else 0
        else:
            i += 1
    return size

def solve_part_2():
    polymer = read_input_file_data()
    atoz = list(string.ascii_lowercase)
    min_length = float('inf')
    for x in atoz:
        new_polymer = [_ for _ in polymer.replace(x, '').replace(x.upper(), '')]
        size = len(new_polymer)
        i = 0
        while i < size - 1:
            c = new_polymer[i]
            d = new_polymer[i + 1]
            if is_polar(c, d):
                new_polymer.pop(i + 1) # remove d
                new_polymer.pop(i)     # remove c
                size -= 2
                i -= 1 if i != 0 else 0
            else:
                i += 1
        if size < min_length:
            min_length = size
    return min_length
    
print(solve_part_2())
