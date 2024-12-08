def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    def extract(line):
        d, i, c = line.split()
        return (d, int(i))

    data = list(map(extract, read_input_file_data().splitlines()))
    
    l = r = u = d = 0
    x = 0
    y = 0
    for direction, i in data:
        if direction == 'L':
            x -= i
            l = min(l, x)
        elif direction == 'R':
            x += i
            r = max(r, x)
        elif direction == 'U':
            y -= i
            u = min(u, y)
        elif direction == 'D':
            y += i
            d = max(d, y)

    DUG = '#'
    UNDUG = '.'

    lr = r - l + 1
    ud = d - u + 1
    diagram = [[UNDUG] * lr for _ in range(ud)] # y, x
    x = abs(l)
    y = abs(u)
    diagram[y][x] = DUG
    for direction, i in data:
        if direction == 'L':
            for _ in range(i):
                x -= 1
                diagram[y][x] = DUG
        elif direction == 'R':
            for _ in range(i):
                x += 1
                diagram[y][x] = DUG
        elif direction == 'U':
            for _ in range(i):
                y -= 1
                diagram[y][x] = DUG
        elif direction == 'D':
            for _ in range(i):
                y += 1
                diagram[y][x] = DUG
                
    # F7
    # LJ
    def get_start_shape(x, y):
        return 'L' if y+1 >= ud or diagram[y+1][x] == UNDUG else 'F'
    def get_end_shape(x, y):
        return 'J' if y+1 >= ud or diagram[y+1][x] == UNDUG else '7'
    def is_change_boundary(s1, s2):
        return (s1 == 'F' and s2 == 'J') or (s1 == 'L' and s2 == '7')

    count = 0
    for y in range(ud):
        x = 0
        is_in = False
        while x < lr:
            if diagram[y][x] == DUG:
                start_shape = get_start_shape(x, y)
                length = 0
                while x < lr and diagram[y][x] == DUG:
                    count += 1
                    x += 1
                    length += 1
                end_shape = get_end_shape(x-1, y)
                if length > 1:
                    if is_change_boundary(start_shape, end_shape):
                        is_in = not is_in
                else:
                    is_in = not is_in
            else:
                if is_in:
                    count += 1
                x += 1
    return count

def solve_part_2():
    data = [(int(line[-2]), int(line[-7: -2], 16)) for line in read_input_file_data().splitlines()]
    
    coordinates = []
    x = 0
    y = 0
    for d, i in data:
        if d == 0: # R
            coordinates.append((y, y, x, x+i))
            x = x + i
        elif d == 1: # D
            coordinates.append((y, y, x, x))
            coordinates.append((y+i, y+i, x, x))
            y = y + i
        elif d == 2: # L
            coordinates.append((y, y, x-i, x))
            x = x - i
        elif d == 3: # U
            coordinates.append((y-i, y-i, x, x))
            coordinates.append((y, y, x, x))
            y = y - i
    coordinates.sort()

    y = coordinates[0][0]
    xes = []
    length = 0
    area = 0
    for y1, y2, x1, x2 in coordinates:
        # Process
        if y1 == y2 and x1 == x2: # Vertical checkpoint
            area += (y1 - y) * length
            y = y1
        else: # Horizontal segment
            if y1 != y:
                area += (y1 - y) * length
                y = y1
            is_combined = False
            insert_index = 0
            for i in range(len(xes)):
                x3, x4 = xes[i]
                if x3 == x2: # Extend left
                    xes[i] = (x1, x4)
                    is_combined = True
                    length += x2 - x1
                    area += x2 - x1
                    # Merge left
                    if i > 0:
                        lx1, lx2 = xes[i-1]
                        if lx2 == x1:
                            length -= 1
                            area -= 1
                            xes[i] = (lx1, x4)
                            xes.pop(i-1)
                    break
                elif x1 == x4: # Extend right
                    xes[i] = (x3, x2)
                    is_combined = True
                    length += x2 - x1
                    area += x2 - x1
                    # Merge right
                    if i < len(xes) - 1:
                        rx1, rx2 = xes[i+1]
                        if x2 == rx1:
                            length -= 1
                            area -= 1
                            xes[i] = (x3, rx2)
                            xes.pop(i+1)
                    break
                elif x1 == x3: # Shrink left inward
                    xes[i] = (x2, x4)
                    is_combined = True
                    length -= x2 - x1
                    if x2 == x4: # Full match
                        xes.pop(i)
                        length -= 1
                    break
                elif x2 == x4: # Shrink right inward
                    xes[i] = (x3, x1)
                    is_combined = True
                    length -= x2 - x1
                    break
                elif x1 > x3 and x2 < x4: # Break segment in middle
                    left = (x3, x1)
                    right = (x2, x4)
                    xes[i] = left
                    xes.insert(i+1, right)
                    is_combined = True
                    length -= x2 - x1 - 1
                    break
                elif x1 > x3: # Did not match
                    insert_index = i + 1
            if not is_combined:
                xes.insert(insert_index, (x1, x2))
                length += x2 - x1 + 1
                area += x2 - x1 + 1
    return area

# def alt():
#     D = [
#         (1, 0),
#         (0, 1),
#         (-1, 0),
#         (0, -1)
#     ]
#     data = [(int(line[-2]), int(line[-7: -2], 16)) for line in read_input_file_data().splitlines()]
#     # d, i
#     x, y = 0, 0
#     a, p = 0, 0
#     for d, i in data:
#         dx, dy = D[d]
#         x += dx*i
#         y += dy*i
#         p += i
#         if d % 2:
#             a += x*dy*i
#     return abs(a)+(p//2)+1
    
print(solve_part_2())
