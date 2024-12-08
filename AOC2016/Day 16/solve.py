from tqdm import tqdm

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

DISK_SIZE = 272

def find_checksum(data):
    if len(data) % 2 == 1:
        return data
    checksum = ""
    for i in range(0, len(data), 2):
        if data[i] == data[i + 1]:
            checksum += '1'
        else:
            checksum += '0'
    return find_checksum(checksum)

def create_b(a: str):
    b = ""
    for c in a:
        if c == '0':
            b = '1' + b
        elif c == '1':
            b = '0' + b
        else:
            raise Exception
    return b

def solve_part_1():
    a = read_input_file_data()
    while len(a) < DISK_SIZE:
        b = create_b(a)
        a += '0' + b
    return find_checksum(a[:DISK_SIZE])

def single_round_checksum(data):
    checksum = ""
    for i in range(0, len(data), 2):
        if data[i] == data[i + 1]:
            checksum += '1'
        else:
            checksum += '0'
    return checksum

A = read_input_file_data()
B = create_b(A)
CHECKSUMS = [['', ''], ['', '']]
for i in range(2):
    for j in range(2):
        CHECKSUMS[i][j] = single_round_checksum(A + str(i) + B + str(j))

def quick_checksum(bit1, bit2):
    return CHECKSUMS[int(bit1)][int(bit2)]

def solve_part_2():
    global DISK_SIZE
    DISK_SIZE = 35651584
    a = A
    b = B
    appended_ints = '0'
    curr_len = len(a) * 2 + 1
    print(f"Current disk size: {curr_len}")
    while curr_len <= DISK_SIZE:
        appended_ints += '0' + create_b(appended_ints)
        curr_len = curr_len * 2 + 1
        print(f"Current disk size: {curr_len}")

    print("Done!\nCalculating checksum...")
    complete_len = DISK_SIZE // (len(a) * 2 + 2)
    complete_index = complete_len * 2
    complete_appends = appended_ints[:complete_index]

    checksum = ""
    for i in tqdm(range(0, complete_index, 2)):
        checksum += quick_checksum(complete_appends[i], complete_appends[i + 1])

    extra = appended_ints[complete_index:complete_index + 2]
    incomplete_len = DISK_SIZE % (len(a) * 2 + 2)
    incomplete = a + extra[0] + b + extra[1]
    incomplete = incomplete[:incomplete_len]

    checksum += single_round_checksum(incomplete)

    print(f"Done!\nReducing checksum...")

    while len(checksum) % 2 == 0:
        checksum = single_round_checksum(checksum)
    
    print(f"Done!\nResulting checksum is:")
    return checksum
    
print(solve_part_2())
