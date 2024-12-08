import math

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    lines = read_input_file_data().splitlines()
    times = list(map(int, lines[0].split()[1:]))
    distances = list(map(int, lines[1].split()[1:]))

    output = 1
    for case in range(len(times)):
        time = times[case]
        distance = distances[case]

        mid_time = math.ceil(time / 2)
        travel = time - mid_time
        assert mid_time * travel > distance

        # Binary search for left time bound that can win
        l = 0
        r = mid_time
        while r - l > 1:
            m = math.floor((l + r) / 2)
            if m * (time - m) > distance: # Win
                r = m
            else:
                l = m
        # l lose, r win
        lbound = r

        # Binary search for right time bound that will lose
        l = mid_time
        r = time
        while r - l > 1:
            m = math.floor((l + r) / 2)
            if m * (time - m) <= distance: # Lose
                r = m
            else:
                l = m
        # l win, r lose
        rbound = r

        ways_of_win = rbound - lbound
        output *= ways_of_win

    return output


def solve_part_2():
    lines = read_input_file_data().splitlines()
    time = int(''.join(lines[0].split()[1:]))
    distance = int(''.join(lines[1].split()[1:]))

    # mid_time = math.ceil(time / 2)
    # travel = time - mid_time
    # assert mid_time * travel > distance

    # # Binary search for left time bound that can win
    # l = 0
    # r = mid_time
    # while r - l > 1:
    #     m = math.floor((l + r) / 2)
    #     if m * (time - m) > distance: # Win
    #         r = m
    #     else:
    #         l = m
    # # l lose, r win
    # lbound = r

    # # Binary search for right time bound that will lose
    # l = mid_time
    # r = time
    # while r - l > 1:
    #     m = math.floor((l + r) / 2)
    #     if m * (time - m) <= distance: # Lose
    #         r = m
    #     else:
    #         l = m
    # # l win, r lose
    # rbound = r

    # ways_of_win = rbound - lbound
    # return ways_of_win

    minx = math.ceil((time - math.sqrt(pow(time, 2) - 4 * distance)) / 2)
    maxx = math.floor((time + math.sqrt(pow(time, 2) - 4 * distance)) / 2)
    return maxx - minx + 1
    
print(solve_part_2())
