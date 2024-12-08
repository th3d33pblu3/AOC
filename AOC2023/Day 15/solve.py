def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    def hash(s: str) -> int:
        value = 0
        for c in s:
            # value += ord(c)
            # value *= 17
            # value %= 256

            value = (value + ord(c)) * 17 % 256
        return value
    
    total_hash = 0
    for s in read_input_file_data().split(','):
        total_hash += hash(s)
    return total_hash

def solve_part_2():
    NUM_BOXES = 256
    def hash(label: str) -> int:
        value = 0
        for c in label:
            value = (value + ord(c)) * 17 % NUM_BOXES
        return value
    
    boxes: list[list[str]] = []
    for _ in range(NUM_BOXES):
        boxes.append([])
    focal_lengths = {}

    for s in read_input_file_data().split(','):
        if s[-1] == '-':
            label = s[:-1]
            box = boxes[hash(label)]
            for i in range(len(box)):
                if box[i] == label:
                    box.pop(i)
                    break
        else: # '='
            label = s[:-2]
            f = int(s[-1])
            box = boxes[hash(label)]
            if label not in box:
                box.append(label)
            focal_lengths[label] = f

    focusing_power = 0
    for b in range(NUM_BOXES):
        f1 = b + 1
        for i, l in enumerate(boxes[b]):
            f2 = i + 1
            f3 = focal_lengths[l]
            focusing_power += f1 * f2 * f3
    return focusing_power

    
print(solve_part_2())
