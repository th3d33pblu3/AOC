def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

OPENERS = ('(', '[', '{', '<')
CLOSERS = (')', ']', '}', '>')

def solve_part_1():
    def find_first_illegal_char(line):
        openers = []
        for char in line:
            if char in OPENERS:
                openers.append(char)
            else:
                correct_opener = OPENERS[CLOSERS.index(char)]
                if (not openers) or (openers[-1] != correct_opener):
                    return char
                openers.pop()
        return None

    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
        None: 0,
    }
    lines = read_input_file_data().splitlines()
    score = 0
    for line in lines:
        score += points[find_first_illegal_char(line)]
    return score

def solve_part_2():
    def is_not_corrupted(line):
        openers = []
        for char in line:
            if char in OPENERS:
                openers.append(char)
            else:
                correct_opener = OPENERS[CLOSERS.index(char)]
                if (not openers) or (openers[-1] != correct_opener):
                    return False
                openers.pop()
        return True
    
    def get_incomplete_openers(line):
        openers = []
        for char in line:
            if char in OPENERS:
                openers.append(char)
            else:
                # correct_opener = OPENERS[CLOSERS.index(char)]
                # if (not openers) or (openers[-1] != correct_opener):
                #     return char
                openers.pop()
        return openers
    
    points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }
    scores = []
    lines = read_input_file_data().splitlines()
    lines = list(filter(is_not_corrupted, lines))
    for line in lines:
        openers = get_incomplete_openers(line)
        openers.reverse()
        curr_score = 0
        for opener in openers:
            closer = CLOSERS[OPENERS.index(opener)]
            curr_score *= 5
            curr_score += points[closer]
        scores.append(curr_score)
    scores.sort()
    return scores[len(scores) // 2]
    
print(solve_part_2())
