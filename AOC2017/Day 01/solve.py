def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

def solve_part_1():
    file = read_input_file()
    data = file.read()
    count = 0
    a = None
    b = int(data[-1])
    for num in data:
        a = b
        b = int(num)
        if a == b:
            count += a
    return count

def solve_part_2():
    file = read_input_file()
    data = file.read()
    count = 0
    a = data[: len(data) // 2]
    b = data[len(data) // 2 :]
    for i in range(len(a)):
        x = int(a[i])
        y = int(b[i])
        if x == y:
            count += x * 2
    return count
    
print(solve_part_2())
