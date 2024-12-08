import re

def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

def is_abba(word):
    if len(word) < 4:
        return False
    else:
        a = ""
        b = word[0]
        c = word[1]
        d = word[2]
        for x in word[3:]:
            a = b
            b = c
            c = d
            d = x
            if a == d and b == c and a != b:
                return True
        return False

def solve_part_1():
    file = read_input_file()
    support = 0
    for line in file.read().splitlines():
        is_abba_inside = False
        is_abba_outside = False
        outside = []
        inside = []

        data = line.split("[")
        outside.append(data[0])
        for segment in data[1:]:
            splitted = segment.split("]")
            inside.append(splitted[0])
            outside.append(splitted[1])
        
        for segment in inside:
            if is_abba(segment):
                is_abba_inside = True
                break
        for segment in outside:
            if is_abba(segment):
                is_abba_outside = True
                break
        if (is_abba_outside and not is_abba_inside):
            support += 1
    return support



def solve_part_2():
    file = read_input_file()
    support = 0
    for line in file.read().splitlines():
        outside = []
        inside = []

        data = line.split("[")
        outside.append(data[0])
        for segment in data[1:]:
            splitted = segment.split("]")
            inside.append(splitted[0])
            outside.append(splitted[1])

        aba_out = []

        def extract_flip_aba_out(word):
            if len(word) < 3:
                return
            a = ""
            b = word[0]
            c = word[1]
            for x in word[2:]:
                a = b
                b = c
                c = x
                if (a == c and a != b):
                    aba_out.append(b + a + b)
        
        def contains_corr_aba(word):
            if len(word) < 3:
                return False
            a = ""
            b = word[0]
            c = word[1]
            for x in word[2:]:
                a = b
                b = c
                c = x
                if (a == c and a != b):
                    aba = a + b + a
                    if aba in aba_out:
                        return True
            return False
        
        for segment in outside:
            extract_flip_aba_out(segment)
        for segment in inside:
            if contains_corr_aba(segment):
                support += 1
                break
    return support
    
print(solve_part_2())
