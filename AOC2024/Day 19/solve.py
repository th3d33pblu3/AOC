def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def solve_part_1():
    supplies, designs = read_input_file_data().split("\n\n")
    supplies = supplies.split(", ")
    designs = designs.splitlines()

    def is_possible(design):
        remaining: set[str] = set()
        remaining.add(design)
        while len(remaining) != 0:
            if "" in remaining:
                return True
            new_remaining = set()
            for r in remaining:
                for pattern in supplies:
                    if r.startswith(pattern):
                        new_remaining.add(r.removeprefix(pattern))
            remaining = new_remaining
        return False

    return len(list(filter(is_possible, designs)))

def solve_part_2():
    supplies, designs = read_input_file_data().split("\n\n")
    supplies = supplies.split(", ")
    designs = designs.splitlines()

    direct_ways = {"": 1}

    def possible_ways(design: str):
        nonlocal direct_ways
        if design in direct_ways:
            return direct_ways[design]
        ways = 0
        for pattern in supplies:
            if design.startswith(pattern):
                ways += possible_ways(design.removeprefix(pattern))
        direct_ways[design] = ways
        return ways

    return sum(list(map(possible_ways, designs)))
    
print(solve_part_2())
