def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def parse_reindeers():
    data = read_input_file_data()
    reindeers = []
    for line in data.splitlines():
        words = line.split()
        speed = int(words[3])
        fly = int(words[6])
        rest = int(words[-2])
        reindeers.append((speed, fly, rest))
    return reindeers

TIME_LIMIT = 2503

def solve_part_1():
    global TIME_LIMIT

    def full_dist_travelled(reindeer):
        speed, fly, rest = reindeer
        return speed * fly * (TIME_LIMIT // (fly + rest))

    def remaining_dist_travelled(reindeer):
        speed, fly, rest = reindeer
        remaining_time = TIME_LIMIT % (fly + rest)
        if remaining_time <= fly:
            return speed * remaining_time
        else:
            return speed * fly
        
    reindeers = parse_reindeers()

    max_dist = 0
    for reindeer in reindeers:
        dist = full_dist_travelled(reindeer) + remaining_dist_travelled(reindeer)
        max_dist = max(max_dist, dist)
    
    return max_dist

def solve_part_2():
    reindeers = parse_reindeers()
    num_reindeers = len(reindeers)
    distances = [0] * num_reindeers
    scores = [0] * num_reindeers
    clock = [0] * num_reindeers

    for _ in range(TIME_LIMIT):
        # Move reindeer
        for i, reindeer in enumerate(reindeers):
            speed, fly, rest = reindeer
            if (clock[i] < fly):
                distances[i] += speed
            
        # Update scores
        max_dist = max(distances)
        for i in range(num_reindeers):
            if distances[i] == max_dist:
                scores[i] += 1

        # Track clock
        for i, reindeer in enumerate(reindeers):
            _, fly, rest = reindeer
            clock[i] = (clock[i] + 1) % (fly + rest)

    return max(scores)

print(solve_part_2())
