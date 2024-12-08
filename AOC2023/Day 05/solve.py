def read_input_file_data():
    FILE = "puzzle_input.txt"
    FILE = "input2.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

class Mapper():
    def __init__(self, inputs: str):
        nums = inputs.splitlines()[1:]
        self.translations = []
        for line in nums:
            self.translations.append(tuple(map(int, line.split())))

    def translate(self, num: int) -> int:
        for dst, src, r in self.translations:
            if num >= src and num < src + r:
                return dst - src + num
        return num
    
    # Part 2
    def translate_range(self, num_ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
        output = []
        for num, num_range in num_ranges:
            L = num             # inclusive
            R = num + num_range # exclusive
            for dst, src, r in self.translations:
                if L == R:
                    break

                offset = dst - src
                SL = src
                SR = src + r

                # Case 1
                #    [-----)      [-----------)   [-----)               [-----)
                # [-----------)   [-----------)   [-----------)   [-----------)
                if SL <= L and SR >= R:
                    # print(f'Case 1: {L=} {R=} {SL=} {SR=}, {num=} {num_range=}, {dst=} {src=} {r=}')
                    output.append((L + offset, R - L))
                    R = L
                    break

                # Case 2
                # [-----------)
                #    [-----)
                elif SL > L and SR < R:
                    # print(f'Case 2: {L=} {R=} {SL=} {SR=}, {num=} {num_range=}, {dst=} {src=} {r=}')
                    output.append((SL + offset, SR - SL))
                    num_ranges.append((SR, R - SR))
                    R = SL
                
                # Case 3
                #    [-----------)   [-----------)
                # [-----------)      [-----)
                elif SL <= L and SR < R and SR > L:
                    # print(f'Case 3: {L=} {R=} {SL=} {SR=}, {num=} {num_range=}, {dst=} {src=} {r=}')
                    output.append((L + offset, SR - L))
                    L = SR
                
                # Case 4
                # [-----------)      [-----------)
                #    [-----------)         [-----)
                elif SL > L and SR >= R and R > SL:
                    # print(f'Case 4: {L=} {R=} {SL=} {SR=}, {num=} {num_range=}, {dst=} {src=} {r=}')
                    output.append((SL + offset, R - SL))
                    R = SL
                
                # Case 5
                # [-----)
                #       [-----)
                # Case 6
                #       [-----)
                # [-----)
                elif R <= SL or L >= SR:
                    pass
                    # print(f'Skipped: {dst=} {src=} {r=}')
                else:
                    raise Exception(f"Unexpected case. {L=} {R=} {SL=}, {SR=}")
            if L != R:
                output.append((L, R - L))
        return list(set(output))

def solve_part_1():
    data = read_input_file_data().split('\n\n')
    seeds = list(map(int, data[0].split()[1:]))
    mappers: list[Mapper] = []
    for i in range(1, len(data)):
        mappers.append(Mapper(data[i]))

    min_loc = float('inf')
    for seed in seeds:
        for mapper in mappers:
            seed = mapper.translate(seed)
        min_loc = min(min_loc, seed)
    return min_loc

def solve_part_2():
    data = read_input_file_data().split('\n\n')
    parsed_seeds = list(map(int, data[0].split()[1:]))
    seed_and_ranges = list(zip(parsed_seeds[::2], parsed_seeds[1::2]))

    mappers: list[Mapper] = []
    for i in range(1, len(data)):
        mappers.append(Mapper(data[i]))

    min_loc = float('inf')
    for seed_and_range in seed_and_ranges:
        seed_and_range = [seed_and_range]
        # print(f"FOR: {seed_and_range=}")
        for mapper in mappers:
            seed_and_range = mapper.translate_range(seed_and_range)
            # print(seed_and_range)
        for loc_and_range in seed_and_range:
            loc = loc_and_range[0]
            min_loc = min(min_loc, loc)
    return min_loc
    
print(solve_part_2())
