def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

def parse_data():
    data = read_input_file_data()
    rules_data, my_ticket_data, nearby_tickets_data = data.split('\n\n')
    rules = []
    for line in rules_data.splitlines():
        field, ranges = line.split(': ')
        range1, range2 = ranges.split(' or ')
        n1, n2 = list(map(int, range1.split('-')))
        n3, n4 = list(map(int, range2.split('-')))
        rules.append((field, (n1, n2), (n3, n4)))
    my_ticket = list(map(int, my_ticket_data.removeprefix('your ticket:\n').split(',')))
    nearby_tickets = list(map(lambda line: list(map(int, line.split(','))), nearby_tickets_data.splitlines()[1:]))
    return rules, my_ticket, nearby_tickets

def solve_part_1():
    rules, my_ticket, nearby_tickets = parse_data()
    ranges = []
    for field, (n1, n2), (n3, n4) in rules:
        ranges.append((n1, n2))
        ranges.append((n3, n4))

    scanning_error_rate = 0
    for ticket in nearby_tickets:
        for val in ticket:
            flag = False
            for n1, n2 in ranges:
                if n1 <= val and val <= n2:
                    flag = True
                    break
            if not flag:
                scanning_error_rate += val
    return scanning_error_rate

def solve_part_2():
    # Parsing inputs
    rules, my_ticket, nearby_tickets = parse_data()

    # Finding valid tickets
    ranges = []
    for field, (n1, n2), (n3, n4) in rules:
        ranges.append((n1, n2))
        ranges.append((n3, n4))

    def is_valid_ticket(ticket):
        nonlocal ranges
        for val in ticket:
            flag = False
            for n1, n2 in ranges:
                if n1 <= val and val <= n2:
                    flag = True
                    break
            if not flag:
                return False
        return True

    valid_tickets = list(filter(is_valid_ticket, nearby_tickets))

    # Finding correct position of the fields
    TICKET_NUMS = len(my_ticket)
    confirmed_field_pos = {}
    unconfirmed_field_pos = {}

    def find_possible_rule_positions(rule):
        nonlocal confirmed_field_pos, unconfirmed_field_pos
        field, (n1, n2), (n3, n4) = rule
        positions = set()
        for pos in range(TICKET_NUMS):
            is_valid_pos = True
            for ticket in valid_tickets:
                if ((n1 <= ticket[pos] and ticket[pos] <= n2) or 
                    (n3 <= ticket[pos] and ticket[pos] <= n4)):
                    continue
                else:
                    is_valid_pos = False
                    break
            if is_valid_pos:
                positions.add(pos)
        if len(positions) == 1:
            confirmed_field_pos[field] = positions.pop()
        else:
            unconfirmed_field_pos[field] = positions

    for rule in rules:
        find_possible_rule_positions(rule)
    
    unconfirmed_fields = set(unconfirmed_field_pos.keys())
    confirmed_positions = set(confirmed_field_pos.values())
    while unconfirmed_fields:
        new_unconfirmed_fields = set()
        for field in unconfirmed_fields:
            remaining_pos = unconfirmed_field_pos[field].difference(confirmed_positions)
            if len(remaining_pos) == 1:
                pos = remaining_pos.pop()
                confirmed_positions.add(pos)
                confirmed_field_pos[field] = pos
            else:
                new_unconfirmed_fields.add(field)
        unconfirmed_fields = new_unconfirmed_fields
    
    # Calculating total value of departure fields multiplied together
    total_value = 1
    for field, _, _ in rules[:6]:
        total_value *= my_ticket[confirmed_field_pos[field]]
    return total_value
    
print(solve_part_2())
