def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    files = read_input_file_data()
    li = 0
    ri = len(files) + 1
    lid = 0
    rid = ri // 2
    buffer = 0

    i = 0
    
    checksum = 0
    while li < ri:
        if li % 2 == 0:
            # Fill files
            for _ in range(int(files[li])):
                checksum += i * lid
                i += 1
            li += 1
        else:
            # Fill empty slot with right buffer
            for _ in range(int(files[li])):
                if buffer == 0:
                    ri -= 2
                    rid -= 1
                    buffer = int(files[ri])
                    if ri < li:
                        return checksum
                checksum += i * rid
                i += 1
                buffer -= 1 
            li += 1
            lid += 1

    # Clear up buffer
    if buffer != 0:
        for _ in range(buffer):
            checksum += i * rid
            i += 1
    
    return checksum

def solve_part_2():
    pass
    
print(solve_part_1())
