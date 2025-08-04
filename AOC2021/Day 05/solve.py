def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def parse_lines():
    def parse_line(line):
        left, right = line.split(' -> ')
        x1, y1 = list(map(int, left.split(',')))
        x2, y2 = list(map(int, right.split(',')))
        return ((x1, y1), (x2, y2))
    return list(map(parse_line, read_input_file_data().splitlines()))

def solve_part_1():
    lines = parse_lines()
    lines = list(filter(lambda line: line[0][0] == line[1][0] or line[0][1] == line[1][1], lines))
    points = {}
    for (x1, y1), (x2, y2) in lines:
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)+1):
                if (x1, y) not in points:
                    points[(x1, y)] = 0
                points[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                if (x, y1) not in points:
                    points[(x, y1)] = 0
                points[(x, y1)] += 1
    return len(list(filter(lambda val: val >= 2, points.values())))

def solve_part_2():
    lines = parse_lines()
    points = {}
    for (x1, y1), (x2, y2) in lines:
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)+1):
                if (x1, y) not in points:
                    points[(x1, y)] = 0
                points[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                if (x, y1) not in points:
                    points[(x, y1)] = 0
                points[(x, y1)] += 1
        else:
            # Make x increasing
            if x2 < x1:
                t = (x1, y1)
                x1 = x2
                y1 = y2
                x2, y2 = t
            
            if y1 < y2:
                dy = 1
            else:
                dy = -1
            for d in range(x2-x1+1):
                p = (x1 + d, y1 + (d * dy))
                if p not in points:
                    points[p] = 0
                points[p] += 1
    return len(list(filter(lambda val: val >= 2, points.values())))
    
print(solve_part_2())
