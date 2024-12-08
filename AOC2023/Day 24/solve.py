def read_input_file_data():
    FILE = "puzzle_input.txt"
    # FILE = "sample.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

MIN = 200000000000000
MAX = 400000000000000

def parse_hailstones():
    hailstones = []
    for line in read_input_file_data().splitlines():
        pos, v = line.split(' @ ')
        x, y, z = tuple(map(int, pos.split(', ')))
        dx, dy, dz = tuple(map(int, v.split(', ')))
        hailstones.append((x, y, z, dx, dy, dz))
    return hailstones

def solve_part_1():
    hailstones = parse_hailstones()
    NUM_HAILSTONES = len(hailstones)
    collisions = 0
    for i in range(NUM_HAILSTONES):
        x1, y1, _, dx1, dy1, _ = hailstones[i]
        for j in range(i + 1, NUM_HAILSTONES):
            x2, y2, _, dx2, dy2, _ = hailstones[j]
            try:
                x = x2 - x1
                y = y2 - y1
                # x = a*dx1 - b*dx2
                # y = a*dy1 - b*dy2

                # a = (x + b*dx2) / dx1
                # b = (y*dx1 - x) / (dx1*dy2 - dx2*dy1)
                
                b = (y*dx1 - x*dy1) / (dx2*dy1 - dy2*dx1)
                a = (x + b*dx2) / dx1
                if a < 0 or b < 0: # Paths crossed in the past
                    continue

                cx = x1 + a*dx1
                cy = y1 + a*dy1
                if (cx >= MIN) and (cx <= MAX) and (cy >= MIN) and (cy <= MAX): # Within range
                    collisions += 1
            except ZeroDivisionError: # Parallel paths
                continue
    return collisions

def solve_part_2():
    pass
    
print(solve_part_1())
