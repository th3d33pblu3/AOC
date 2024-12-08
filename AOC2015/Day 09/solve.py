from itertools import permutations
from math import inf

def read_input_file():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    return file

def parse_line(line):
    words = line.split()
    locA = words[0]
    locB = words[2]
    dist = int(words[4])
    return locA, locB, dist

def get_locations_and_distances():
    distances = {}
    file = read_input_file()
    for line in file.read().splitlines():
        locA, locB, dist = parse_line(line)
        if distances.get(locA) == None:
            distances[locA] = {locB: dist}
        else:
            distances.get(locA)[locB] = dist
        if distances.get(locB) == None:
            distances[locB] = {locA: dist}
        else:
            distances.get(locB)[locA] = dist
    
    locations = list(distances.keys())
    return locations, distances

def solve_part_1():
    locations, distances = get_locations_and_distances()
    paths = permutations(locations)

    def distance_of_path(path):
        assert len(path) > 2
        total_dist = 0
        start = path[0]
        for loc in path[1:]:
            total_dist += distances[start][loc]
            start = loc
        return total_dist
    
    min_dist = inf
    for path in paths:
        dist = distance_of_path(list(path))
        min_dist = min(min_dist, dist)

    return min_dist

def solve_part_2():
    locations, distances = get_locations_and_distances()
    paths = permutations(locations)

    def distance_of_path(path):
        assert len(path) > 2
        total_dist = 0
        start = path[0]
        for loc in path[1:]:
            total_dist += distances[start][loc]
            start = loc
        return total_dist
    
    max_dist = 0
    for path in paths:
        dist = distance_of_path(list(path))
        max_dist = max(max_dist, dist)

    return max_dist
    
print(solve_part_2())
