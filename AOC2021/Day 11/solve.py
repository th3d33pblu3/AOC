def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

DELTAS = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))
WIDTH = 10
HEIGHT = 10
def get_neighbours(x, y):
    neighbours = []
    for dx, dy in DELTAS:
        nx, ny = x + dx, y + dy
        if 0 <= nx and nx < WIDTH and 0 <= ny and ny < HEIGHT:
            neighbours.append((nx, ny))
    return neighbours

def solve_part_1():
    octopus = [list(map(int, line)) for line in read_input_file_data().splitlines()]
    flashes = 0
    for _ in range(100):
        # Increase brightness
        frontier = set() # Octopus to flash
        for y in range(HEIGHT):
            for x in range(WIDTH):
                octopus[y][x] += 1
                if octopus[y][x] == 10:
                    frontier.add((x, y))
        
        # Increasing flashes
        seen = set()
        while frontier:
            new_frontier = set()
            for x, y in frontier: # Flash
                neighbours = get_neighbours(x, y)
                for nx, ny in neighbours:
                    octopus[ny][nx] += 1
                    if octopus[ny][nx] >= 10:
                        new_frontier.add((nx, ny))
            seen.update(frontier)
            new_frontier.difference_update(seen)
            frontier = new_frontier

        # Reset flashes
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if octopus[y][x] >= 10:
                    octopus[y][x] = 0
                    flashes += 1
    return flashes

def solve_part_2():
    octopus = [list(map(int, line)) for line in read_input_file_data().splitlines()]
    steps = 0
    while True:
        # Increase brightness
        frontier = set() # Octopus to flash
        for y in range(HEIGHT):
            for x in range(WIDTH):
                octopus[y][x] += 1
                if octopus[y][x] == 10:
                    frontier.add((x, y))
        
        # Increasing flashes
        seen = set()
        while frontier:
            new_frontier = set()
            for x, y in frontier: # Flash
                neighbours = get_neighbours(x, y)
                for nx, ny in neighbours:
                    octopus[ny][nx] += 1
                    if octopus[ny][nx] >= 10:
                        new_frontier.add((nx, ny))
            seen.update(frontier)
            new_frontier.difference_update(seen)
            frontier = new_frontier

        # Reset flashes
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if octopus[y][x] >= 10:
                    octopus[y][x] = 0
        
        # Count steps
        steps += 1
        if all(list(map(lambda line: all(list(map(lambda i: i == 0, line))), octopus))):
            return steps
    
print(solve_part_2())
