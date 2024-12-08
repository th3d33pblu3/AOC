import time

def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

def get_sensors_and_beacons():
    """
    Returns a list of sensors and their corresponding closest beacon location.
    Coordinates are given as (x, y) for the sensors and beacons.
    """
    file = read_input_file()
    sensors = []
    beacons = []
    for line in file.read().splitlines():
        words = line.split()
        sx_word, sy_word, bx_word, by_word = words[2], words[3], words[-2], words[-1]
        sx, sy = int(sx_word[2:-1]), int(sy_word[2:-1])
        sensors.append((sx, sy))
        bx, by = int(bx_word[2:-1]), int(by_word[2:  ])
        beacons.append((bx, by))

    return sensors, beacons

# Part 1 helper functions
Y_TARGET = 2000000

def find_range_covering_target(sensor, beacon):
    sx, sy = sensor
    bx, by = beacon

    dist = abs(sx - bx) + abs(sy - by)
    if abs(Y_TARGET - sy) <= dist:
        remaining_x_dist = dist - abs(Y_TARGET - sy)
        return (sx - remaining_x_dist, sx + remaining_x_dist)
    else:
        return None

def is_intersecting_range(range1, range2):
    left_r1, right_r1 = range1
    left_r2, right_r2 = range2
    # if (left_r1 <= left_r2 <= right_r1) or (left_r1 <= right_r2 <= right_r1) or (left_r2 <= left_r1 <= right_r2) or (left_r2 <= right_r1 <= right_r2):
    #     return True
    # else:
    #     return False
    if (right_r1 < left_r2) or (right_r2 < left_r1):
        return False
    else:
        return True

def combine_range(range1, range2):
    left, right = zip(*[range1, range2])
    return (min(left), max(right))

def is_in_range(val, range):
    if val < range[0] or val > range[1]:
        return False
    else:
        return True




# Part 2 helper functions
LIMIT = 4000000

# def find_range_covered(sensor, beacon):
#     """
#     Range: ((x_min, x_max), y)
#     """
#     sx, sy = sensor
#     bx, by = beacon
#     dist = abs(sx - bx) + abs(sy - by)

#     ranges = set()
#     top = (sx, sy - dist)
#     left = (sx - dist, sy)
#     bot = (sx, sy + dist)

#     curr_range = [[top[0], top[0]], top[1]]
#     while curr_range[1] < left[1]:
#         ranges.add(((curr_range[0][0], curr_range[0][1]), curr_range[1]))
#         curr_range[0][0] -= 1
#         curr_range[0][1] += 1
#         curr_range[1] += 1
#     while curr_range[1] <= bot[1]:
#         ranges.add(((curr_range[0][0], curr_range[0][1]), curr_range[1]))
#         curr_range[0][0] += 1
#         curr_range[0][1] -= 1
#         curr_range[1] += 1

#     return ranges

def remove_range(range, range_to_remove):
    """
    Range: (x_min, x_max)
    """
    left_r1, right_r1 = range
    left_r2, right_r2 = max(0, range_to_remove[0]), min(LIMIT, range_to_remove[1])

    if left_r2 <= left_r1 and right_r1 <= right_r2:    # Range fully covered by range to remove
        return None
    elif (right_r1 < left_r2) or (right_r2 < left_r1): # Not intersecting
        return [range]
    else:                                              # Intersecting
        if left_r1 < left_r2 and right_r1 > right_r2:  # Range fully containing range to remove
            return [(left_r1, left_r2 - 1), (right_r2 + 1, right_r1)]
        else:                                          # Partially intersecting
            if left_r2 <= left_r1 <= right_r2:         # Left portion removed
                return [(right_r2 + 1, right_r1)] 
            elif left_r1 <= left_r2 <= right_r1:       # Right portion removed
                return [(left_r1, left_r2 - 1)] 
            else:
                raise Exception("Unexpected range intersection")





def solve_part_1():
    sensors, beacons = get_sensors_and_beacons()
    target_ranges = []

    # Find the range in the target row covered by the scan
    for sensor, beacon in zip(sensors, beacons):
        target_range_covered = find_range_covering_target(sensor, beacon)
        if target_range_covered != None:
            target_ranges.append(target_range_covered)
    
    # If there is no cover, return 0
    if len(target_ranges) == 0:
        return 0

    # Beacons in the target range
    beacons_in_target_range = set()
    for beacon in beacons:
        if beacon[1] == Y_TARGET:
            beacons_in_target_range.add(beacon)
    
    # Count the number of crossed out locations
    crossed_out_count = 0
    next_queue = []
    while len(target_ranges) != 0 or len(next_queue) != 0:
        if len(target_ranges) == 0:
            target_ranges = next_queue
            next_queue = []

        # Combine the relevant ranges
        current_range = target_ranges.pop(0)
        repeat_loop = True
        mem_len = len(target_ranges)
        while repeat_loop:
            for range in target_ranges:
                if is_intersecting_range(current_range, range):
                    current_range = combine_range(current_range, range)
                else:
                    next_queue.append(range)
            if len(next_queue) == mem_len:
                repeat_loop = False
            else:
                target_ranges = next_queue
                next_queue = []
                mem_len = len(target_ranges)

        # Remove beacons in the current range
        remove_count = 0
        for beacon in beacons_in_target_range:
            if is_in_range(beacon[0], current_range):
                remove_count += 1

        crossed_out_count += current_range[1] - current_range[0] + 1 - remove_count
        target_ranges = []

    return crossed_out_count # 4919281

def solve_part_2():
    start_time = time.time()

    possible_coordinates = []
    for _ in range(LIMIT + 1):
        possible_coordinates.append([(0, LIMIT)])

    print(f"Initialization complete, performing range removal...")
    time1 = time.time()
    print(f"Time taken      : {time1 - start_time}")
    print(f"Total time taken: {time1 - start_time}")

    num_sensors_removed = 0

    prev_time = time1
    sensors, beacons = get_sensors_and_beacons()
    # Find the range covered by the scan
    for sensor, beacon in zip(sensors, beacons):
        sx, sy = sensor
        bx, by = beacon
        dist = abs(sx - bx) + abs(sy - by)
        for y_dif in range(dist + 1):
            x_dif = dist - y_dif
            scanned_range = (sx - x_dif, sx + x_dif)
            for y in [sy - y_dif, sy + y_dif]:
                if 0 <= y <= LIMIT:
                    new_row = []
                    for existing_range in possible_coordinates[y]:
                        new_ranges = remove_range(existing_range, scanned_range)
                        if new_ranges != None:
                            new_row.extend(new_ranges)
                    possible_coordinates[y] = new_row
        num_sensors_removed += 1
        print(f"Number of sensor ranges removed: {num_sensors_removed}")
        curr_time = time.time()
        print(f"Time taken      : {curr_time - prev_time}")
        prev_time = curr_time
    
    time2 = time.time()
    print(f"Total time taken: {time2 - start_time}")

    to_return = None
    for index, row in enumerate(possible_coordinates):
        if len(row) != 0:
            if (len(row) == 1 and row[0][0] == row[0][1]):
                print(f"x={row[0][0]}, y={index}")
                to_return = row[0][0] * LIMIT + index
            else:
                print(f"Unexpected answer with x-range={row}, y={index}")
    return to_return # 12630143363767
    
print(solve_part_2())
