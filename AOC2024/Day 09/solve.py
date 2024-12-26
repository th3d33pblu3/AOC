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
    files = []
    empty = []
    id_files = []
    id_empty = []

    data = list(map(int, read_input_file_data()))
    
    files = data[::2]
    empty = data[1::2]
    block_pos = [None] * len(data)

    s = 0
    for i in range(len(data)):
        if i % 2 == 0:
            file_size = files[i // 2]
            block_pos[i] = s
            s += file_size
        else:
            empty_size = empty[(i - 1) // 2]
            block_pos[i] = s
            s += empty_size

    def get_file_checksum(file_id, file_size, pos):
        return file_id * (pos + pos + file_size - 1) * file_size // 2
    
    checksum = 0
    for i in range(len(files) - 1, -1, -1):
        file_size = files[i]
        for j in range(i):
            empty_size = empty[j]
            if empty_size >= file_size:
                empty[j] = empty_size - file_size
                pos = block_pos[j * 2 + 1]
                block_pos[j * 2 + 1] = pos + file_size

                # add checksum
                checksum += get_file_checksum(i, file_size, pos)
                break
        else:
            # did not move file
            checksum += get_file_checksum(i, file_size, block_pos[i * 2])
    
    return checksum
    
print(solve_part_2())
