import re

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    # Get answer after skipping 10830 iterations
    stars = list(map(lambda line: list(map(int, re.findall(r"-?\d+", line))), read_input_file_data().splitlines()))
    t = 0
    while(True):
        # Move stars
        t += 1
        for star in stars:
            star[0] += star[2]
            star[1] += star[3]
        if input(f"Current iteration: {t} Skip some iterations? y/n") == 'y':
            skips = input("How many?\n")
            if skips.isdigit():
                skips = int(skips)
                print(f"Skip {skips} itertions")
                t += skips
                for star in stars:
                    star[0] += star[2] * skips
                    star[1] += star[3] * skips

        # Get range
        max_x = max(s[0] for s in stars)
        min_x = min(s[0] for s in stars)
        max_y = max(s[1] for s in stars)
        min_y = min(s[1] for s in stars)
        width = max_x - min_x + 1
        length = max_y - min_y + 1
        print(f"{length=} {width=}")
        if input("Display current setup? y/n\n") == 'y':
            display = [['.'] * width for _ in range(length)]
            for star in stars:
                display[star[1] - min_y][star[0] - min_x] = '#'
            for line in display:
                print(''.join(line))

def solve_part_2():
    return 10831 # result from part 1
    
print(solve_part_2())
