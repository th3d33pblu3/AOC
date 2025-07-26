def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def parse_data():
    rules_data, messages_data = read_input_file_data().split('\n\n')
    rules = rules_data.splitlines()
    messages = messages_data.splitlines()
    return rules, messages

def solve_part_1():
    rules, messages = parse_data()

    # Defining rules
    specific_rules = {}
    pending_rules = {}
    affected = {}
    for line in rules:
        id, desc = line.split(": ")
        id = int(id)
        if desc.startswith('"'):
            specific_rules[id] = [desc.strip('"')]
        else:
            pending_rules[id] = list(map(lambda part: list(map(int, part.split())), desc.split(" | ")))
            for part in pending_rules[id]:
                for r in part:
                    s = affected.get(r, set())
                    s.add(id)
                    affected[r] = s

    # Defining specific rules
    frontier = set()
    for id in specific_rules:
        frontier.update(affected[id])
    while frontier:
        new_frontier = set()
        for id in frontier:
            parts = pending_rules[id]
            required_rule_ids = set()
            for part in parts:
                required_rule_ids.update(part)
            if not all(list(map(lambda n: n in specific_rules, list(required_rule_ids)))):
                continue
            specific_rule = set()
            for part in parts:
                part_specifics = ['']
                for rule_id in part:
                    rule_specifics = specific_rules[rule_id]
                    part_specifics = [p + r for p in part_specifics for r in rule_specifics]
                specific_rule.update(part_specifics)
            specific_rules[id] = specific_rule
            if id != 0:
                new_frontier.update(affected[id])
        frontier = new_frontier.difference(specific_rules)

    # Computation
    count = 0
    for message in messages:
        if message in specific_rules[0]:
            count += 1
    return count

def solve_part_2():
    '''
    Replace:
    8: 42     with 8: 42 | 42 8
    11: 42 31 with 11: 42 31 | 42 11 31
    Affected:
    0: 8 11

    This tells us that 0 now matches strings with 
    x*42 + y*42 + y*31, where x and y > 0
    '''
    # Still define rules the same way as before
    rules, messages = parse_data()

    # Defining rules
    specific_rules = {}
    pending_rules = {}
    affected = {}
    for line in rules:
        id, desc = line.split(": ")
        id = int(id)
        if desc.startswith('"'):
            specific_rules[id] = [desc.strip('"')]
        else:
            pending_rules[id] = list(map(lambda part: list(map(int, part.split())), desc.split(" | ")))
            for part in pending_rules[id]:
                for r in part:
                    s = affected.get(r, set())
                    s.add(id)
                    affected[r] = s

    # Defining specific rules
    frontier = set()
    for id in specific_rules:
        frontier.update(affected[id])
    while frontier:
        new_frontier = set()
        for id in frontier:
            parts = pending_rules[id]
            required_rule_ids = set()
            for part in parts:
                required_rule_ids.update(part)
            if not all(list(map(lambda n: n in specific_rules, list(required_rule_ids)))):
                continue
            specific_rule = set()
            for part in parts:
                part_specifics = ['']
                for rule_id in part:
                    rule_specifics = specific_rules[rule_id]
                    part_specifics = [p + r for p in part_specifics for r in rule_specifics]
                specific_rule.update(part_specifics)
            specific_rules[id] = specific_rule
            if id != 0:
                new_frontier.update(affected[id])
        frontier = new_frontier.difference(specific_rules)
    
    # Use new computation
    count = 0
    rule42 = specific_rules[42]
    rule31 = specific_rules[31]
    # print(rule42)
    # print(rule31)
    # print(list(map(len, rule42)))
    # print(list(map(len, rule31)))
    # print(set(rule42).intersection(set(rule31)))
    '''
    On further inspection, each specific string in 
    rule 42 and 31 contain exactly 8 characters.
    Also, there are no overlaps between strings in 
    rule 42 and 31.
    '''
    SEGMENT_SIZE = 8
    for message in messages:
        if len(message) % SEGMENT_SIZE != 0:
            continue
        num_segments = len(message) // SEGMENT_SIZE
        segments = [message[i*SEGMENT_SIZE: (i+1)*SEGMENT_SIZE] for i in range(num_segments)]
        count42 = 0
        count31 = 0
        ptr = 0
        while ptr < num_segments and segments[ptr] in rule42:
            count42 += 1
            ptr += 1
        while ptr < num_segments and segments[ptr] in rule31:
            count31 += 1
            ptr += 1
        if ptr != num_segments:
            continue
        if count42 > count31 and count42 != 0 and count31 != 0:
            count += 1
    return count
    
print(solve_part_2())
