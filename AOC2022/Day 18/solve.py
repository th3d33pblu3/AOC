from queue import Queue
import numpy as np

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def get_scan_sizes():
    max_x = 0
    max_y = 0
    max_z = 0
    for line in read_input_file_data().splitlines():
        x, y, z = tuple(map(int, line.split(",")))
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
        if z > max_z:
            max_z = z
    return max_x + 1 + 2, max_y + 1 + 2, max_z + 1 + 2

def solve_part_1():
    numx, numy, numz = get_scan_sizes()

    scan = np.zeros((numx, numy, numz))
    for line in read_input_file_data().splitlines():
        x, y, z = tuple(map(int, line.split(",")))
        scan[x + 1, y + 1, z + 1] = 1
    
    open_sides = 0
    DELTA = [-1, 1]
    for x in range(1, numx - 1):
        for y in range(1, numy - 1):
            for z in range(1, numz - 1):
                if scan[x, y, z] == 1:
                    for dx in DELTA:
                        if scan[x + dx, y,      z] == 0:
                            open_sides += 1
                    for dy in DELTA:
                        if scan[x,      y + dy, z] == 0:
                            open_sides += 1
                    for dz in DELTA:
                        if scan[x,      y,      z + dz] == 0:
                            open_sides += 1
    
    return open_sides

def solve_part_2():
    numx, numy, numz = get_scan_sizes()

    scan = np.zeros((numx, numy, numz))
    for line in read_input_file_data().splitlines():
        x, y, z = tuple(map(int, line.split(",")))
        scan[x + 1, y + 1, z + 1] = 1

    def get_touching_points(point):
        x, y, z = point
        pts = []
        DELTA = [-1, 1]
        for dx in DELTA:
            if 0 <= x + dx < numx:
                pts.append((x + dx, y, z))
        for dy in DELTA:
            if 0 <= y + dy < numy:
                pts.append((x, y + dy, z))
        for dz in DELTA:
            if 0 <= z + dz < numz:
                pts.append((x, y, z + dz))
        return pts

    def get_scanned_value(point):
        return scan[point[0], point[1], point[2]]
    
    open_sides = 0
    frontier = Queue()
    frontier.put((0, 0, 0))
    while frontier.qsize() != 0:
        point = frontier.get()
        point_value = get_scanned_value(point)
        if point_value == 2:
            continue
        touching_points = get_touching_points(point)
        for other_point in touching_points:
            scanned_value = get_scanned_value(other_point)
            if scanned_value == 0:
                frontier.put(other_point)
            elif scanned_value == 1:
                open_sides += 1
            else:
                pass
        scan[point[0], point[1], point[2]] = 2
    return open_sides
    
print(solve_part_2())
