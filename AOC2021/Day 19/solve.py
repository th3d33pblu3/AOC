def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    scanners = [[tuple(map(int, coordinates.split(','))) for coordinates in sc.splitlines()[1:]] for sc in read_input_file_data().split('\n\n')]
    ORIENTATIONS = [
        (0, 1, 2,  1,  1,  1), #  x,  y,  z
        (0, 2, 1,  1,  1, -1), #  x,  z, -y
        (0, 1, 2,  1, -1, -1), #  x, -y, -z
        (0, 2, 1,  1, -1,  1), #  x, -z,  y

        (0, 1, 2, -1,  1, -1), # -x,  y, -z
        (0, 2, 1, -1, -1, -1), # -x, -z, -y
        (0, 1, 2, -1, -1,  1), # -x, -y,  z
        (0, 2, 1, -1,  1,  1), # -x,  z,  y

        (1, 2, 0,  1,  1,  1), #  y,  z,  x
        (1, 0, 2,  1,  1, -1), #  y,  x, -z
        (1, 2, 0,  1, -1, -1), #  y, -z, -x
        (1, 0, 2,  1, -1,  1), #  y, -x,  z

        (1, 2, 0, -1,  1, -1), # -y,  z, -x
        (1, 0, 2, -1,  1,  1), # -y,  x,  z
        (1, 2, 0, -1, -1,  1), # -y, -z,  x
        (1, 0, 2, -1, -1, -1), # -y, -x, -z

        (2, 0, 1,  1,  1,  1), #  z,  x,  y
        (2, 1, 0,  1, -1,  1), #  z, -y,  x
        (2, 0, 1,  1, -1, -1), #  z, -x, -y
        (2, 1, 0,  1,  1, -1), #  z,  y, -x

        (2, 0, 1, -1, -1,  1), # -z, -x,  y
        (2, 1, 0, -1,  1,  1), # -z,  y,  x
        (2, 0, 1, -1,  1, -1), # -z,  x, -y
        (2, 1, 0, -1, -1, -1), # -z, -y, -x
    ]

    def convert(curr_beacon, target_beacon, orientation, scanner):
        tx, ty, tz, dx, dy, dz = orientation
        cb = curr_beacon
        tb = target_beacon
        return list(map(lambda sb: (sb[tx]*dx - cb[tx]*dx + tb[0], sb[ty]*dy - cb[ty]*dy + tb[1], sb[tz]*dz - cb[tz]*dz + tb[2]), scanner))

    discovered_beacons = set(scanners.pop(0)) # Using scanner 0 as identifier

    def try_match_scanner(scanner):
        nonlocal discovered_beacons
        for target_beacon in discovered_beacons:
            for curr_beacon in scanner:
                for orientation in ORIENTATIONS:
                    result = convert(curr_beacon, target_beacon, orientation, scanner)
                    if len(discovered_beacons.intersection(result)) >= 12:
                        discovered_beacons.update(result)
                        return None
        return scanner
    
    while scanners:
        scanner = scanners.pop(0)
        result = try_match_scanner(scanner)
        if result:
            scanners.append(scanner)

    return len(discovered_beacons)

def solve_part_2():
    scanners = [[tuple(map(int, coordinates.split(','))) for coordinates in sc.splitlines()[1:]] for sc in read_input_file_data().split('\n\n')]
    ORIENTATIONS = [
        (0, 1, 2,  1,  1,  1), #  x,  y,  z
        (0, 2, 1,  1,  1, -1), #  x,  z, -y
        (0, 1, 2,  1, -1, -1), #  x, -y, -z
        (0, 2, 1,  1, -1,  1), #  x, -z,  y

        (0, 1, 2, -1,  1, -1), # -x,  y, -z
        (0, 2, 1, -1, -1, -1), # -x, -z, -y
        (0, 1, 2, -1, -1,  1), # -x, -y,  z
        (0, 2, 1, -1,  1,  1), # -x,  z,  y

        (1, 2, 0,  1,  1,  1), #  y,  z,  x
        (1, 0, 2,  1,  1, -1), #  y,  x, -z
        (1, 2, 0,  1, -1, -1), #  y, -z, -x
        (1, 0, 2,  1, -1,  1), #  y, -x,  z

        (1, 2, 0, -1,  1, -1), # -y,  z, -x
        (1, 0, 2, -1,  1,  1), # -y,  x,  z
        (1, 2, 0, -1, -1,  1), # -y, -z,  x
        (1, 0, 2, -1, -1, -1), # -y, -x, -z

        (2, 0, 1,  1,  1,  1), #  z,  x,  y
        (2, 1, 0,  1, -1,  1), #  z, -y,  x
        (2, 0, 1,  1, -1, -1), #  z, -x, -y
        (2, 1, 0,  1,  1, -1), #  z,  y, -x

        (2, 0, 1, -1, -1,  1), # -z, -x,  y
        (2, 1, 0, -1,  1,  1), # -z,  y,  x
        (2, 0, 1, -1,  1, -1), # -z,  x, -y
        (2, 1, 0, -1, -1, -1), # -z, -y, -x
    ]

    def convert(curr_beacon, target_beacon, orientation, scanner):
        tx, ty, tz, dx, dy, dz = orientation
        cb = curr_beacon
        tb = target_beacon
        return list(map(lambda sb: (sb[tx]*dx - cb[tx]*dx + tb[0], sb[ty]*dy - cb[ty]*dy + tb[1], sb[tz]*dz - cb[tz]*dz + tb[2]), scanner))

    discovered_beacons = set(scanners.pop(0)) # Using scanner 0 as identifier
    scanner_positions = {(0, 0, 0)}

    def try_match_scanner(scanner):
        nonlocal discovered_beacons
        for target_beacon in discovered_beacons:
            for curr_beacon in scanner:
                for orientation in ORIENTATIONS:
                    result = convert(curr_beacon, target_beacon, orientation, scanner)
                    if len(discovered_beacons.intersection(result)) >= 12:
                        discovered_beacons.update(result)
                        # Finding location of scanner
                        tx, ty, tz, dx, dy, dz = orientation
                        cb = curr_beacon
                        tb = target_beacon
                        return (tb[0] - cb[tx]*dx, tb[1] - cb[ty]*dy, tb[2] - cb[tz]*dz)
        return None
    
    while scanners:
        scanner = scanners.pop(0)
        scanner_pos = try_match_scanner(scanner)
        if scanner_pos:
            scanner_positions.add(scanner_pos)
        else:
            scanners.append(scanner)

    largest_md = 0
    for s1 in scanner_positions:
        for s2 in scanner_positions:
            if s1 == s2:
                continue
            largest_md = max(abs(s2[0] - s1[0]) + abs(s2[1] - s1[1]) + abs(s2[2] - s1[2]), largest_md)
    return largest_md
    
print(solve_part_2())
