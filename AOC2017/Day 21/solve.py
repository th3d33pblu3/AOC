from math import sqrt

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

INIT_ART = [".#.", "..#", "###"]

def get_enhancement(times):
    rules = read_input_file_data().splitlines()
    actual_rules = {}
    for line in rules:
        f, t = line.split(" => ")
        # Direct map
        f1 = f
        # Rotate clockwise
        f2 = '/'.join(''.join(x) for x in zip(*f.split('/')[::-1]))
        # Rotate anti-clockwise
        f3 = '/'.join([''.join(x) for x in zip(*f.split('/'))][::-1])
        # Rotate 180 degrees
        f4 = f[::-1]

        # Flipped
        ff = '/'.join(f.split('/')[::-1])
        # Direct map
        f5 = ff
        # Rotate clockwise
        f6 = '/'.join(''.join(x) for x in zip(*ff.split('/')[::-1]))
        # Rotate anti-clockwise
        f7 = '/'.join([''.join(x) for x in zip(*ff.split('/'))][::-1])
        # Rotate 180 degrees
        f8 = ff[::-1]
    
        actual_rules[f1] = t
        actual_rules[f2] = t
        actual_rules[f3] = t
        actual_rules[f4] = t
        actual_rules[f5] = t
        actual_rules[f6] = t
        actual_rules[f7] = t
        actual_rules[f8] = t
    
    def get_sections(art):
        size = len(art)
        sections = []
        if size % 2 == 0:
            # divisible by 2
            for i in range(0, size, 2):
                for j in range(0, size, 2):
                    sections.append(f"{art[i][j:j+2]}/{art[i+1][j:j+2]}")
        else:
            # divisible by 3
            for i in range(0, size, 3):
                for j in range(0, size, 3):
                    sections.append(f"{art[i][j:j+3]}/{art[i+1][j:j+3]}/{art[i+2][j:j+3]}")
        return sections

    def combine_sections(sections):
        size = int(sqrt(len(sections)))
        return [
            ''.join(row)
            for i in range(0, len(sections), size)
            for row in zip(*[s.split('/') for s in sections[i:i + size]])
        ]

    def enhance(art):
        return combine_sections(list(map(lambda s: actual_rules[s], get_sections(art))))

    art = INIT_ART
    for _ in range(times):
        art = enhance(art)
    return sum([r.count("#") for r in art])

def solve_part_1():
    return get_enhancement(5)

def solve_part_2():
    return get_enhancement(18)
    
print(solve_part_2())
