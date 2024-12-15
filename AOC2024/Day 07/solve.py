def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    data = read_input_file_data().splitlines()
    total = 0
    for eq in data:
        r, nums = eq.split(": ")
        r = int(r)
        nums = list(map(int, nums.split()))
        s = set()
        s.add(nums.pop(0))
        for i in nums:
            new_s = set()
            for si in s:
                new_s.add(si + i)
                new_s.add(si * i)
            s = new_s
        if r in s:
            total += r
    return total

def solve_part_2():
    data = read_input_file_data().splitlines()
    total = 0
    for eq in data:
        r, nums = eq.split(": ")
        r = int(r)
        nums = list(map(int, nums.split()))
        s = set()
        s.add(nums.pop(0))
        for i in nums:
            new_s = set()
            for si in s:
                new_s.add(si + i)
                new_s.add(si * i)
                new_s.add(int(str(si) + str(i)))
            s = new_s
        if r in s:
            total += r
    return total
    
print(solve_part_2())
