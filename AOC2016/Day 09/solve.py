def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

def solve_part_1():
    file = read_input_file()
    skip = 0
    length = 0
    braces = ""
    read_braces = False
    for char in file.read():
        if skip != 0:
            skip -= 1
            continue
        if char == "(":
            read_braces = True
        elif char == ")":
            read_braces = False
            mul = braces.split("x")
            chars = int(mul[0])
            times = int(mul[1])
            skip = chars
            length += chars * times
            braces = ""
        elif read_braces:
            braces += char
        else:
            length += 1

    return length

def solve_part_2():
    file = read_input_file()
    code = file.read()

    def decompress(code):
        length = 0
        skip = 0
        braces = ""
        read_braces = False
        for i, char in enumerate(code):
            if skip != 0:
                skip -= 1
                continue
            if char == "(":
                read_braces = True
            elif char == ")":
                read_braces = False
                mul = braces.split("x")
                chars = int(mul[0])
                times = int(mul[1])
                skip = chars
                length += decompress(code[i + 1 : i + 1 + chars]) * times
                braces = ""
            elif read_braces:
                braces += char
            else:
                length += 1

        return length

    return decompress(code)
    
print(solve_part_2())
