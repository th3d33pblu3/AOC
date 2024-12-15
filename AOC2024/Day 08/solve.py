def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    antenna_map = read_input_file_data().splitlines()
    HEIGHT = len(antenna_map)
    WIDTH = len(antenna_map[0])

    antennas = {}
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if antenna_map[i][j] == '.':
                continue
            label = antenna_map[i][j]
            if label not in antennas:
                antennas[label] = {(i, j)}
            else:
                antennas[label].add((i, j))

    antinodes = set()
    for s in antennas.values():
        ls = list(s)
        length = len(ls)
        for a in range(length):
            y1, x1 = ls[a]
            for b in range(a+1, length):
                y2, x2 = ls[b]
                
                dy = y1 - y2
                dx = x1 - x2
                antinodes.add((y1+dy, x1+dx))
                antinodes.add((y2-dy, x2-dx))
    return len(list(filter(lambda p: p[0] >= 0 and p[0] < HEIGHT and p[1] >= 0 and p[1] < WIDTH, antinodes)))

def solve_part_2():
    antenna_map = read_input_file_data().splitlines()
    HEIGHT = len(antenna_map)
    WIDTH = len(antenna_map[0])

    antennas = {}
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if antenna_map[i][j] == '.':
                continue
            label = antenna_map[i][j]
            if label not in antennas:
                antennas[label] = {(i, j)}
            else:
                antennas[label].add((i, j))

    antinodes = set()
    for s in antennas.values():
        ls = list(s)
        length = len(ls)
        for a in range(length):
            y1, x1 = ls[a]
            for b in range(a+1, length):
                y2, x2 = ls[b]
                
                dy = y1 - y2
                dx = x1 - x2
                
                antinodes.add((y1, x1))
                antinodes.add((y2, x2))

                yi, xi = y1+dy, x1+dx
                while yi >= 0 and yi < HEIGHT and xi >= 0 and xi < WIDTH:
                    antinodes.add((yi, xi))
                    yi += dy
                    xi += dx
                
                yi, xi = y2-dy, x2-dx
                while yi >= 0 and yi < HEIGHT and xi >= 0 and xi < WIDTH:
                    antinodes.add((yi, xi))
                    yi -= dy
                    xi -= dx
    return len(antinodes)
    
print(solve_part_2())
