def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def parse_data():
    data = read_input_file_data()
    rules = {}
    for line in data.splitlines():
        line = line.strip('.')
        outer_bag, contents = line.split(' contain ')
        outer_bag = outer_bag.removesuffix(' bag')
        outer_bag = outer_bag.removesuffix(' bags')
        content_info = {}
        if contents != 'no other bags':
            for part in contents.split(', '):
                n, color = part.split(' ', 1)
                n = int(n)
                color = color.removesuffix(' bag')
                color = color.removesuffix(' bags')
                content_info[color] = n
        rules[outer_bag] = content_info
    return rules

def solve_part_1():
    rules = parse_data()
    seen = set()
    frontier = set(filter(lambda rule: 'shiny gold' in rules[rule], rules.keys()))
    seen.update(frontier)
    while frontier:
        new_frontier = set()
        for color in frontier:
            new_frontier.update(set(filter(lambda rule: color in rules[rule], rules.keys())))
        new_frontier.difference_update(seen)
        seen.update(frontier)
        frontier = new_frontier
    return len(seen)

def solve_part_2():
    rules = parse_data()
    frontier = []
    frontier.append(('shiny gold', 1))
    bag_count = 0
    while frontier:
        new_frontier = []
        for bag, multiple in frontier:
            bag_count += multiple
            for inner_bag, count in rules[bag].items():
                new_frontier.append((inner_bag, count * multiple))
        frontier = new_frontier
    return bag_count - 1
    
print(solve_part_2())
