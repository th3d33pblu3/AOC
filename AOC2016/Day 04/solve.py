from collections import Counter
import re

def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

def solve_part_1():
    id_sum = 0
    file = read_input_file()
    for line in file.read().splitlines():
        data = line.split("-")
        characters = "".join(data[:-1])
        check = re.search("(?<=\[)(.*)(?=\])", data[-1]).group(0)
        id = int(re.search("[0-9]*", data[-1]).group(0))
        most_common_5 = sorted(Counter(characters).most_common(), key=lambda x: (-x[1], x[0]))[0: 5]
        result = ''.join(list(map(lambda x: x[0], most_common_5)))
        if (result == check):
            id_sum += id
    return id_sum

def write(data, name):
    FILE = f"./Day 04/{name}.txt"
    file = open(FILE, "w")
    file.write(data)
    file.close()

def make_output_file():
    output = ""
    file = read_input_file()
    for line in file.read().splitlines():
        data = line.split("-")
        characters = "".join(data[:-1])
        check = re.search("(?<=\[)(.*)(?=\])", data[-1]).group(0)
        most_common_5 = sorted(Counter(characters).most_common(), key=lambda x: (-x[1], x[0]))[0: 5]
        result = ''.join(list(map(lambda x: x[0], most_common_5)))
        if (result == check):
            output += line + "\n"
    write(output[:-1], "real_rooms")

def rotate(word, rotations):
    return ''.join(list(map(lambda x: chr(((ord(x) - ord('a') + rotations) % 26) + ord('a')), list(word))))

def solve_part_2():
    output = ""
    real_rooms_file = open("./Day 04/real_rooms.txt", 'r')
    for line in real_rooms_file.read().splitlines():
        data = line.split("-")
        words = data[:-1]
        rotations = int(re.search("[0-9]*", data[-1]).group(0))
        decrypted_name = "-".join(list(map(lambda word: rotate(word, rotations), words)))
        output += f"{decrypted_name} {rotations}\n"
    output = output[:-1]
    write(output, "real_rooms_decrypted")
    return output
    
print(solve_part_2())
