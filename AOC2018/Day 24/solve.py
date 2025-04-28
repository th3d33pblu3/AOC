import re

def read_input_file_data():
    FILE = "puzzle_input.txt"
    file = open(FILE, "r")
    data = file.read()
    file.close()
    return data

class Group:
    def __init__(self, units, hp, atk, initiative, atk_type, weaknesses, immunities):
        self.units = units
        self.hp = hp
        self.atk = atk
        self.initiative = initiative
        self.atk_type = atk_type
        self.weaknesses = weaknesses
        self.immunities = immunities

    def boost(self, boost_amount):
        self.atk += boost_amount

def parse_line(line):
    units, hp, atk, initiative = list(map(int, re.findall(r'\d+', line)))
    atk_type = re.search(r'attack that does \d+ ([a-z]*) damage', line).group(1)
    pattern = re.findall(r'weak to ([^;\)]+)', line)
    weaknesses = pattern[0].split(', ') if pattern else []
    pattern = re.findall(r'immune to ([^;\)]+)', line)
    immunities = pattern[0].split(', ') if pattern else []
    return Group(units, hp, atk, initiative, atk_type, weaknesses, immunities)

def parse_data():
    data = read_input_file_data()
    immune_system, infection = data.split('\n\n')
    immune_system = [parse_line(line) for line in immune_system.splitlines()[1:]]
    infection = [parse_line(line) for line in infection.splitlines()[1:]]
    return immune_system, infection

def solve_part_1():
    immune_system, infection = parse_data()

    while immune_system and infection:
        # ----- Target selection phase ------
        selections = set() # (attacker, target)

        # Immune system select target
        immune_system.sort(key=lambda g: (g.units * g.atk, g.initiative), reverse=True)
        avail_targets = infection.copy()
        for group in immune_system:
            selected_target = None
            for target in avail_targets:
                if group.atk_type in target.immunities:
                    continue
                if selected_target == None:
                    selected_target = target
                else:
                    if (group.atk_type in selected_target.weaknesses) != (group.atk_type in target.weaknesses):
                        # only one group is weak
                        if group.atk_type in target.weaknesses: # select group with weakness
                            selected_target = target
                    elif selected_target.units * selected_target.atk != target.units * target.atk:
                        # groups have different effective power
                        if target.units * target.atk > selected_target.units * selected_target.atk: # select group with larget effective power
                            selected_target = target
                    else:
                        if target.initiative > selected_target.initiative: # select group with higher initiative
                            selected_target = target
            if selected_target:
                selections.add((group, selected_target))
                avail_targets.remove(selected_target)

        # Infection select target
        infection.sort(key=lambda g: (g.units * g.atk, g.initiative), reverse=True)
        avail_targets = immune_system.copy()
        for group in infection:
            selected_target = None
            for target in avail_targets:
                if group.atk_type in target.immunities:
                    continue
                if selected_target == None:
                    selected_target = target
                else:
                    if (group.atk_type in selected_target.weaknesses) != (group.atk_type in target.weaknesses):
                        # only one group is weak
                        if group.atk_type in target.weaknesses: # select group with weakness
                            selected_target = target
                    elif selected_target.units * selected_target.atk != target.units * target.atk:
                        # groups have different effective power
                        if target.units * target.atk > selected_target.units * selected_target.atk: # select group with larget effective power
                            selected_target = target
                    else:
                        if target.initiative > selected_target.initiative: # select group with higher initiative
                            selected_target = target
            if selected_target:
                selections.add((group, selected_target))
                avail_targets.remove(selected_target)

        # ----- Attacking phase ------
        attack_seq: list[tuple[Group, Group]] = list(selections)
        attack_seq.sort(key=lambda selection: selection[0].initiative, reverse=True)
        for attacker, target in attack_seq:
            if attacker.units <= 0:
                continue
            damage = attacker.units * attacker.atk * (2 if attacker.atk_type in target.weaknesses else 1)
            target.units -= damage // target.hp

        # ----- Filter out dead groups -----
        immune_system = list(filter(lambda group: group.units > 0, immune_system))
        infection = list(filter(lambda group: group.units > 0, infection))

    return sum(map(lambda group: group.units, immune_system)) + sum(map(lambda group: group.units, infection))

def solve_part_2():
    immune_system, infection = parse_data()
    low = 0
    high = max([group.hp for group in infection])

    def get_battle_result(boost_amount):
        immune_system, infection = parse_data()
        # ----- Boost immune system ------
        for group in immune_system:
            group.boost(boost_amount)

        while immune_system and infection:
            # ----- Target selection phase ------
            selections = set() # (attacker, target)

            # Immune system select target
            immune_system.sort(key=lambda g: (g.units * g.atk, g.initiative), reverse=True)
            avail_targets = infection.copy()
            for group in immune_system:
                selected_target = None
                for target in avail_targets:
                    if group.atk_type in target.immunities:
                        continue
                    if selected_target == None:
                        selected_target = target
                    else:
                        if (group.atk_type in selected_target.weaknesses) != (group.atk_type in target.weaknesses):
                            # only one group is weak
                            if group.atk_type in target.weaknesses: # select group with weakness
                                selected_target = target
                        elif selected_target.units * selected_target.atk != target.units * target.atk:
                            # groups have different effective power
                            if target.units * target.atk > selected_target.units * selected_target.atk: # select group with larget effective power
                                selected_target = target
                        else:
                            if target.initiative > selected_target.initiative: # select group with higher initiative
                                selected_target = target
                if selected_target:
                    selections.add((group, selected_target))
                    avail_targets.remove(selected_target)

            # Infection select target
            infection.sort(key=lambda g: (g.units * g.atk, g.initiative), reverse=True)
            avail_targets = immune_system.copy()
            for group in infection:
                selected_target = None
                for target in avail_targets:
                    if group.atk_type in target.immunities:
                        continue
                    if selected_target == None:
                        selected_target = target
                    else:
                        if (group.atk_type in selected_target.weaknesses) != (group.atk_type in target.weaknesses):
                            # only one group is weak
                            if group.atk_type in target.weaknesses: # select group with weakness
                                selected_target = target
                        elif selected_target.units * selected_target.atk != target.units * target.atk:
                            # groups have different effective power
                            if target.units * target.atk > selected_target.units * selected_target.atk: # select group with larget effective power
                                selected_target = target
                        else:
                            if target.initiative > selected_target.initiative: # select group with higher initiative
                                selected_target = target
                if selected_target:
                    selections.add((group, selected_target))
                    avail_targets.remove(selected_target)

            # ----- Attacking phase ------
            attack_seq: list[tuple[Group, Group]] = list(selections)
            attack_seq.sort(key=lambda selection: selection[0].initiative, reverse=True)

            is_any_units_dead = False
            for attacker, target in attack_seq:
                if attacker.units <= 0:
                    continue
                damage = attacker.units * attacker.atk * (2 if attacker.atk_type in target.weaknesses else 1)
                target.units -= damage // target.hp
                if damage // target.hp > 0:
                    is_any_units_dead = True
            if not is_any_units_dead: # No units die, end in draw
                return []

            # ----- Filter out dead groups -----
            immune_system = list(filter(lambda group: group.units > 0, immune_system))
            infection = list(filter(lambda group: group.units > 0, infection))

        return immune_system
    
    while high - low > 1:
        mid = (low + high) // 2
        immune_system = get_battle_result(mid)
        if immune_system:
            high = mid
        else:
            low = mid
    return sum([group.units for group in get_battle_result(high)])

print(solve_part_2())
