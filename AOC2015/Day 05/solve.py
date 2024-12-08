def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

def solve_part_1():
    file = read_input_file()

    VOWELS = ['a', 'e', 'i', 'o', 'u']
    FORBIDDEN = ['ab', 'cd', 'pq', 'xy']

    def is_vowel(char):
        for vowel in VOWELS:
            if char == vowel:
                return True
        return False

    def is_forbidden(chars):
        for substring in FORBIDDEN:
            if chars == substring:
                return True
        return False

    count = 0
    for line in file.readlines():
        vowels = 0
        for char in line:
            if is_vowel(char):
                vowels += 1

        is_double = False
        is_nauty = False
        for i in range(len(line) - 1):
            x = line[i]
            y = line[i + 1]
            if x == y:
                is_double = True
            if is_forbidden(x + y):
                is_nauty = True
                break

        if (is_nauty):
            continue
        
        if (is_double and vowels >= 3):
            count += 1
    
    return count

def solve_part_2():
    file = read_input_file()

    count = 0

    for line in file.readlines():
        cond2 = False
        for i in range(len(line) - 2):
            x = line[i]
            y = line[i + 2]
            if x == y:
                cond2 = True
                break
        
        cond1 = False
        index = 0
        counter = {}
        while (index < len(line) - 1):
            pair = line[index] + line[index + 1]
            if counter.get(pair) == None:
                counter[pair] = index
            else:
                if index > counter.get(pair) + 1:
                    cond1 = True
                    break
            index += 1

        if (cond1 and cond2):
            count += 1
        
    return count

    
print(solve_part_2())
