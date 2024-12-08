import queue

def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

def solve_part_1():
    file = read_input_file()
    data = file.read()
    first = data[0]
    i = 1
    a = first
    b = first
    c = first
    d = first
    while not (a != b and a != c and a != d and b != c and b != d and c != d):
        a = b
        b = c
        c = d
        d = data[i]
        i += 1
    return i

def letter_to_index(char):
    return ord(char) - ord('a')

def solve_part_2():
    file = read_input_file()
    data = file.read()
    array = [0] * 26
    q = queue.Queue()
    def put(char):
        array[letter_to_index(char)] += 1
    def remove(char):
        array[letter_to_index(char)] -= 1
    def is_done():
        for i in array:
            if (i != 1 and i != 0):
                return False
        return True

    UNIQUE = 14

    i = UNIQUE
    for char in data[0 : i]:
        put(char)
        q.put(char)
    while not is_done():
        remove(q.get())
        char = data[i]
        put(char)
        q.put(char)
        i += 1

    return i

print(solve_part_2())