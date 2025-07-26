def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    adaptors = list(map(int, read_input_file_data().splitlines()))
    adaptors.sort()
    adaptors.append(adaptors[-1] + 3)
    adaptors.insert(0, 0)

    diffs = [None, 0, 0, 0]
    for i in range(len(adaptors) - 1):
        diffs[adaptors[i+1] - adaptors[i]] += 1
    return diffs[1] * diffs[3]

def solve_part_2():
    adaptors = list(map(int, read_input_file_data().splitlines()))
    adaptors.sort()
    adaptors.append(adaptors[-1] + 3)
    adaptors.insert(0, 0)
    LIMIT = len(adaptors) - 1

    ways = {}
    def get_ways(index, low):
        if (index, low) in ways:
            return ways[(index, low)]
        if index >= LIMIT:
            ways[(index, low)] = 1
            return 1
        if adaptors[index+1] - adaptors[index] == 3 or adaptors[index] - low == 3:
            temp = get_ways(index+1, adaptors[index])
            ways[(index, low)] = temp
            return temp
        else:
            temp = get_ways(index+1, low) + get_ways(index+1, adaptors[index])
            ways[(index, low)] = temp
            return temp
    return get_ways(1, 0)
    
print(solve_part_2())
