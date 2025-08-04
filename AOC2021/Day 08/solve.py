def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    data = read_input_file_data().splitlines()
    count = 0
    for line in data:
        _, outputs = line.split(" | ")
        outputs = outputs.split()
        for output in outputs:
            if len(output) in (2, 4, 3, 7):
                count += 1
    return count

def solve_part_2():
    def process_wiring(displays):
        one = next(filter(lambda d: len(d) == 2, displays))
        four = next(filter(lambda d: len(d) == 4, displays))
        seven = next(filter(lambda d: len(d) == 3, displays))
        eight = next(filter(lambda d: len(d) == 7, displays))

        two_three_five = list(filter(lambda d: len(d) == 5, displays))
        zero_six_nine = list(filter(lambda d: len(d) == 6, displays))

        a = set(seven).difference(set(one)).pop() # Difference between 7 and 1
        f = next(filter(lambda char: all([char in n for n in zero_six_nine]), one)) # The segment in 1 that is in all of 0 6 and 9
        c = set(one).difference(set(f)).pop() # The other segment in 1
        three = next(filter(lambda n: (c in n) and (f in n), two_three_five)) # The only one in 2, 3, 5 containing 1
        d = set(three).intersection(set(four)).difference(set(one)).pop()
        g = set(three).difference(set((a, c, d, f))).pop()
        b = set(four).difference(set((c, d, f))).pop()
        e = set(eight).difference(set((a, b, c, d, f, g))).pop()
        
        return {
            0: set((a, b, c, e, f, g)),
            1: set((c, f)),
            2: set((a, c, d, e, g)),
            3: set((a, c, d, f, g)),
            4: set((b, c, d, f)),
            5: set((a, b, d, f, g)),
            6: set((a, b, d, e, f, g)),
            7: set((a, c, f)),
            8: set((a, b, c, d, e, f, g)),
            9: set((a, b, c, d, f, g))
        }

    data = read_input_file_data().splitlines()
    total = 0
    for line in data:
        displays, outputs = line.split(" | ")
        displays = displays.split()
        outputs = outputs.split()
        wiring = process_wiring(displays)

        output_value = 0
        for output in outputs:
            output_value *= 10
            key = set(output)
            for i in range(10):
                if key == wiring[i]:
                    output_value += i
                    break
        
        total += output_value
    return total
    
print(solve_part_2())
