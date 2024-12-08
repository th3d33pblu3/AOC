def read_input_file_data():
    FILE = "puzzle_input.txt"
    FILE = "sample.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

GOOD = '.'
BAD = '#'
UNKNOWN = '?'

def solve_part_1():
    def parse(line: str) -> tuple[list[str], list[int]]:
        data = line.split()
        springs = [c for c in data[0]]
        records = list(map(int, data[1].split(',')))
        return springs, records
    
    def solve_range_records(springs: list[str], ranges: list[tuple[int, int]], records: list[int]) -> int:
        if len(records) == 0:
            for i, j in ranges:
                if BAD in springs[i : j]:
                    return 0
            return 1
        if len(ranges) == 0:
            return 0
        
        i, j = ranges[0][0], ranges[0][1]
        r = records[0]

        if j - i < r:
            if BAD in springs[i : j]:
                return 0
            return solve_range_records(springs, ranges[1:], records)
        elif j - i == r:
            if BAD in springs[i : j]:
                return solve_range_records(springs, ranges[1:], records[1:])
            return solve_range_records(springs, ranges[1:], records[1:]) + solve_range_records(springs, ranges[1:], records)
        else: # j - i > r
            # First ?
            unknown = None
            for x in range(i, j):
                if springs[x] == UNKNOWN:
                    unknown = x
                    break
            if unknown == None:
                return 0
            
            # Good
            springs[unknown] = GOOD
            r1 = ranges.copy()
            i, j = r1.pop(0)
            if unknown + 1 != j:
                r1.insert(0, (unknown + 1, j))
            if i != unknown:
                r1.insert(0, (i, unknown))
            count_good = solve_range_records(springs, r1, records)

            # Bad
            springs[unknown] = BAD
            count_bad = solve_range_records(springs, ranges, records)

            # Revert change
            springs[unknown] = UNKNOWN
            return count_good + count_bad

    def find_num_arrangements(springs: list[str], records: list[int]) -> int:
        ranges = []
        i = 0
        while i < len(springs):
            if springs[i] in (BAD, UNKNOWN):
                keep = i
                while i < len(springs) and springs[i] in (BAD, UNKNOWN):
                    i += 1
                ranges.append((keep, i))
            i += 1
        return solve_range_records(springs, ranges, records)

    ways = 0
    for line in read_input_file_data().splitlines():
        springs, records = parse(line)
        ways += find_num_arrangements(springs, records)
    return ways

def solve_part_2():
    def parse_and_unfold(line: str) -> tuple[list[str], list[int]]:
        data = line.split()
        unfolded_springs = [c for c in UNKNOWN.join([data[0]] * 5)]
        unfolded_records = list(map(int, ','.join([data[1]] * 5).split(',')))
        return unfolded_springs, unfolded_records
    
    def solve_range_records(springs: list[str], ranges: list[tuple[int, int]], records: list[int]) -> int:
        if len(records) == 0:
            for i, j in ranges:
                if BAD in springs[i : j]:
                    return 0
            return 1
        if len(ranges) == 0:
            return 0
        
        i, j = ranges[0][0], ranges[0][1]
        r = records[0]

        if j - i < r:
            if BAD in springs[i : j]:
                return 0
            return solve_range_records(springs, ranges[1:], records)
        elif j - i == r:
            if BAD in springs[i : j]:
                return solve_range_records(springs, ranges[1:], records[1:])
            return solve_range_records(springs, ranges[1:], records[1:]) + solve_range_records(springs, ranges[1:], records)
        else: # j - i > r
            # First ?
            unknown = None
            for x in range(i, j):
                if springs[x] == UNKNOWN:
                    unknown = x
                    break
            if unknown == None:
                return 0
            
            # Good
            springs[unknown] = GOOD
            r1 = ranges.copy()
            i, j = r1.pop(0)
            if unknown + 1 != j:
                r1.insert(0, (unknown + 1, j))
            if i != unknown:
                r1.insert(0, (i, unknown))
            count_good = solve_range_records(springs, r1, records)

            # Bad
            springs[unknown] = BAD
            count_bad = solve_range_records(springs, ranges, records)

            # Revert change
            springs[unknown] = UNKNOWN
            return count_good + count_bad

    def find_num_arrangements(springs: list[str], records: list[int]) -> int:
        ranges = []
        i = 0
        while i < len(springs):
            if springs[i] in (BAD, UNKNOWN):
                keep = i
                while i < len(springs) and springs[i] in (BAD, UNKNOWN):
                    i += 1
                ranges.append((keep, i))
            i += 1
        return solve_range_records(springs, ranges, records)

    ways = 0
    for line in read_input_file_data().splitlines():
        springs, records = parse_and_unfold(line)
        # t = find_num_arrangements(springs, records)
        # print(t)
        # ways += t
        ways += find_num_arrangements(springs, records)
    return ways
    
print(solve_part_2())
