def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    orbits = {b: a for a, b in list(map(lambda line: tuple(line.split(")")), read_input_file_data().splitlines()))}
    orbit_counts = {"COM": 0}
    objects = orbits.keys()

    def count_orbits(object):
        if object in orbit_counts:
            return orbit_counts[object]
        else:
            count = count_orbits(orbits[object]) + 1
            orbit_counts[object] = count
            return count

    total_count = 0
    for object in objects:
        total_count += count_orbits(object)
    return total_count

def solve_part_2():
    orbits = {b: a for a, b in list(map(lambda line: tuple(line.split(")")), read_input_file_data().splitlines()))}
    
    you_path = set()
    curr = "YOU"
    while curr != "COM":
        curr = orbits[curr]
        you_path.add(curr)
    
    san_path = set()
    curr = "SAN"
    while curr != "COM":
        curr = orbits[curr]
        san_path.add(curr)

    diff1 = you_path.difference(san_path)
    diff2 = san_path.difference(you_path)
    return len(diff1) + len(diff2)
    
print(solve_part_2())
