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
    hailstones = parse_hailstones()
    s1, s2, s3 = hailstones[:3]
    p1, v1 = ((s2[0] - s1[0], s2[1] - s1[1], s2[2] - s1[2]), (s2[3] - s1[3], s2[4] - s1[4], s2[5] - s1[5])) # s2 - s1
    p2, v2 = ((s3[0] - s1[0], s3[1] - s1[1], s3[2] - s1[2]), (s3[3] - s1[3], s3[4] - s1[4], s3[5] - s1[5])) # s3 - s1

    # Under specific t1 and t2, these two vectors are parallel and cross product = 0
    # (p1 + v1 * t1) x (p2 + v2 * t2) = 0
    # (p1 x p2) + t1 * (v1 x p2) + t2 * (p1 x v2) + t1 * t2 * (v1 x v2) = 0
    # Using property of (a x b) ⋅ a = 0
    # Equation 1 by dot product of v2:
    # (p1 x p2) ⋅ v2 + t1 * (v1 x p2) ⋅ v2 = 0
    # t1 = - [(p1 x p2) ⋅ v2] / [(v1 x p2) ⋅ v2]
    # Equation 2 by dot product of v1:
    # (p1 x p2) ⋅ v1 + t2 * (p1 x v2) ⋅ v1 = 0
    # t2 = - [(p1 x p2) ⋅ v1] / [(p1 x v2) ⋅ v1]
    
    def dot(a, b):
        return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
    def cross(a, b):
        return a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]
    
    t1 = - dot(cross(p1, p2), v2) // dot(cross(v1, p2), v2)
    t2 = - dot(cross(p1, p2), v1) // dot(cross(p1, v2), v1)
    assert t1 % 1 == 0 and t2 % 1 == 0
    t1 = int(t1)
    t2 = int(t2)
    
    def add(a, b):
        return a[0] + b[0], a[1] + b[1], a[2] + b[2]
    def scale(a, c):
        return a[0] * c, a[1] * c, a[2] * c
    def diff(a, b):
        return a[0] - b[0], a[1] - b[1], a[2] - b[2]
    
    stone1 = add(p1, scale(v1, t1)) # relative to s1
    stone2 = add(p2, scale(v2, t2)) # relative to s1
    v = scale(diff(stone1, stone2), 1 / (t1 - t2)) # relative to s1
    assert v[0] % 1 == 0 and v[1] % 1 == 0 and v[2] % 1 == 0
    v = tuple(map(int, v))
    x = add(stone1, scale(v, -t1)) # relative to s1
    V = add(v, s1[3:]) # actual
    X = add(x, s1[:3]) # actual
    return X[0] + X[1] + X[2]

print(solve_part_2())
