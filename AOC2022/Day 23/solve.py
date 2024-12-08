from collections import Counter

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def is_elf(char):
    return char == "#"

def parse_input():
    elfs = set()
    for y, line in enumerate(read_input_file_data().splitlines()):
        for x, char in enumerate(line):
            if is_elf(char):
                elfs.add((x, y))
    return elfs

def solve_part_1():
    SEARCH_DIRECTIONS = 4
    ROUNDS = 10

    elfs = parse_input()

    def has_elf_around(elf):
        x, y = elf
        for y_dif in [-1, 1]:
            for x_dif in [-1, 0, 1]:
                if (x + x_dif, y + y_dif) in elfs:
                    return True
        for x_dif in [-1, 1]:
            if (x + x_dif, y) in elfs:
                return True
        return False
    
    def propose(elf, search_seq):
        x, y = elf
        for _ in range(SEARCH_DIRECTIONS):
            if search_seq == 0: # North
                y_dif = -1
                for x_dif in [-1, 0, 1]:
                    if (x + x_dif, y + y_dif) in elfs:
                        search_seq = (search_seq + 1) % SEARCH_DIRECTIONS
                        break
                else:
                    return (x, y - 1)
            elif search_seq == 1: # South
                y_dif = 1
                for x_dif in [-1, 0, 1]:
                    if (x + x_dif, y + y_dif) in elfs:
                        search_seq = (search_seq + 1) % SEARCH_DIRECTIONS
                        break
                else:
                    return (x, y + 1)
            elif search_seq == 2: # West
                x_dif = -1
                for y_dif in [-1, 0, 1]:
                    if (x + x_dif, y + y_dif) in elfs:
                        search_seq = (search_seq + 1) % SEARCH_DIRECTIONS
                        break
                else:
                    return (x - 1, y)
            elif search_seq == 3: # East
                x_dif = 1
                for y_dif in [-1, 0, 1]:
                    if (x + x_dif, y + y_dif) in elfs:
                        search_seq = (search_seq + 1) % SEARCH_DIRECTIONS
                        break
                else:
                    return (x + 1, y)
            else:
                raise Exception(f"Unknown search seq: {search_seq}")
        return None
    
    curr_search_seq = 0
    for _ in range(10):
        proposals = {}
        proposals_count = Counter()
        for elf in elfs:
            if has_elf_around(elf):
                proposal = propose(elf, curr_search_seq)
                if proposal != None:
                    proposals[elf] = proposal
                    proposals_count[proposal] += 1
        if len(proposals) == 0:
            break
        for elf in proposals.keys():
            proposal = proposals.get(elf)
            if proposals_count.get(proposal) == 1:
                elfs.remove(elf)
                elfs.add(proposal)
        curr_search_seq = (curr_search_seq + 1) % SEARCH_DIRECTIONS

    elfs = list(elfs)
    elfs_count = len(elfs)
    min_x, min_y = elfs[0]
    max_x, max_y = elfs[0]
    for elf in elfs:
        x, y = elf
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y
    return (max_x - min_x + 1) * (max_y - min_y + 1) - elfs_count

def solve_part_2():
    SEARCH_DIRECTIONS = 4

    elfs = parse_input()

    def has_elf_around(elf):
        x, y = elf
        for y_dif in [-1, 1]:
            for x_dif in [-1, 0, 1]:
                if (x + x_dif, y + y_dif) in elfs:
                    return True
        for x_dif in [-1, 1]:
            if (x + x_dif, y) in elfs:
                return True
        return False
    
    def propose(elf, search_seq):
        x, y = elf
        for _ in range(SEARCH_DIRECTIONS):
            if search_seq == 0: # North
                y_dif = -1
                for x_dif in [-1, 0, 1]:
                    if (x + x_dif, y + y_dif) in elfs:
                        search_seq = (search_seq + 1) % SEARCH_DIRECTIONS
                        break
                else:
                    return (x, y - 1)
            elif search_seq == 1: # South
                y_dif = 1
                for x_dif in [-1, 0, 1]:
                    if (x + x_dif, y + y_dif) in elfs:
                        search_seq = (search_seq + 1) % SEARCH_DIRECTIONS
                        break
                else:
                    return (x, y + 1)
            elif search_seq == 2: # West
                x_dif = -1
                for y_dif in [-1, 0, 1]:
                    if (x + x_dif, y + y_dif) in elfs:
                        search_seq = (search_seq + 1) % SEARCH_DIRECTIONS
                        break
                else:
                    return (x - 1, y)
            elif search_seq == 3: # East
                x_dif = 1
                for y_dif in [-1, 0, 1]:
                    if (x + x_dif, y + y_dif) in elfs:
                        search_seq = (search_seq + 1) % SEARCH_DIRECTIONS
                        break
                else:
                    return (x + 1, y)
            else:
                raise Exception(f"Unknown search seq: {search_seq}")
        return None
    
    curr_search_seq = 0
    rounds = 0
    while True:
        rounds += 1
        proposals = {}
        proposals_count = Counter()
        for elf in elfs:
            if has_elf_around(elf):
                proposal = propose(elf, curr_search_seq)
                if proposal != None:
                    proposals[elf] = proposal
                    proposals_count[proposal] += 1
        if len(proposals) == 0:
            break
        for elf in proposals.keys():
            proposal = proposals.get(elf)
            if proposals_count.get(proposal) == 1:
                elfs.remove(elf)
                elfs.add(proposal)
        curr_search_seq = (curr_search_seq + 1) % SEARCH_DIRECTIONS

    return rounds
    
print(solve_part_2())
