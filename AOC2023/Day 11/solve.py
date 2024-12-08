def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

SPACE = '.'
GALAXY = '#'

def solve_part_1():
    observation = [[_ for _ in line] for line in read_input_file_data().splitlines()]
    rows = len(observation)
    columns = len(observation[0])

    has_galaxy_rows = [False] * rows
    has_galaxy_cols = [False] * columns
    galaxies = []
    for x in range(rows):
        for y in range(columns):
            if observation[x][y] == GALAXY:
                has_galaxy_rows[x] = True
                has_galaxy_cols[y] = True
                galaxies.append((x, y))
    
    expand_rows = set()
    for r in range(rows):
        if not has_galaxy_rows[r]:
            expand_rows.add(r)
    expand_cols = set()
    for c in range(columns):
        if not has_galaxy_cols[c]:
            expand_cols.add(c)
    
    # Expand row and col
    expanded_galaxies = []
    for galaxy in galaxies:
        x, y = galaxy
        inc_x = 0
        inc_y = 0
        for r in expand_rows:
            if r < x:
                inc_x += 1
        for c in expand_cols:
            if c < y:
                inc_y += 1
        expanded_galaxies.append((x + inc_x, y + inc_y))

    num_galaxies = len(expanded_galaxies)
    distances = 0
    for i in range(num_galaxies - 1):
        galaxy1 = expanded_galaxies[i]
        for j in range(i + 1, num_galaxies):
            galaxy2 = expanded_galaxies[j]
            distances += abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])
    
    return distances

def solve_part_2():
    observation = [[_ for _ in line] for line in read_input_file_data().splitlines()]
    rows = len(observation)
    columns = len(observation[0])

    has_galaxy_rows = [False] * rows
    has_galaxy_cols = [False] * columns
    galaxies = []
    for x in range(rows):
        for y in range(columns):
            if observation[x][y] == GALAXY:
                has_galaxy_rows[x] = True
                has_galaxy_cols[y] = True
                galaxies.append((x, y))
    
    expand_rows = set()
    for r in range(rows):
        if not has_galaxy_rows[r]:
            expand_rows.add(r)
    expand_cols = set()
    for c in range(columns):
        if not has_galaxy_cols[c]:
            expand_cols.add(c)
    
    # Expand row and col
    EXPANSION_RATE = 1000000
    EXPANSION_EFFECTIVENESS = EXPANSION_RATE - 1
    expanded_galaxies = []
    for galaxy in galaxies:
        x, y = galaxy
        inc_x = 0
        inc_y = 0
        for r in expand_rows:
            if r < x:
                inc_x += 1
        for c in expand_cols:
            if c < y:
                inc_y += 1
        expanded_galaxies.append((x + inc_x * EXPANSION_EFFECTIVENESS, y + inc_y * EXPANSION_EFFECTIVENESS))

    num_galaxies = len(expanded_galaxies)
    distances = 0
    for i in range(num_galaxies - 1):
        galaxy1 = expanded_galaxies[i]
        for j in range(i + 1, num_galaxies):
            galaxy2 = expanded_galaxies[j]
            distances += abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])
    
    return distances
    
print(solve_part_2())
